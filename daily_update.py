import yfinance as yf
import csv
import json

INPUT_CSV = "nse_companies.csv"
OUTPUT_JSON = "final_cleaned_data.json"

def read_all_tickers():
    tickers = []
    with open(INPUT_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tickers.append({
                "Company Name": row["companyName"].strip(),
                "Ticker": row["Symbol"].strip()
            })
    return tickers

def fetch_company_data(entry):
    ticker = entry["Ticker"]
    stock = yf.Ticker(ticker)
    info = stock.info

    try:
        total_revenue = stock.financials.loc["Total Revenue"].iloc[0]
    except Exception:
        total_revenue = None

    fields = {
        "Company Name": info.get("longName"),
        "Ticker": ticker,
        "Sector": info.get("sector"),
        "Debt to Equity": info.get("debtToEquity"),
        "Profit Margin": round(info.get("profitMargins", 0) * 100, 2) if info.get("profitMargins") is not None else None,
        "P/E Ratio": info.get("trailingPE"),
        "Market Cap": round(info.get("marketCap", 0) / 1e7, 2) if info.get("marketCap") is not None else None,
        "Revenue": round(total_revenue / 1e7, 2) if total_revenue is not None else None,
        "Promoter Holding": round(info.get("heldPercentInsiders", 0) * 100, 2) if info.get("heldPercentInsiders") is not None else None
    }

    if all(v is not None for v in fields.values()):
        return fields
    return None

def calculate_score(company):
    score = 0

    try:
        pe = float(company.get("P/E Ratio"))
    except (TypeError, ValueError):
        pe = None

    try:
        de = float(company.get("Debt to Equity"))
    except (TypeError, ValueError):
        de = None

    try:
        pm = float(company.get("Profit Margin"))
    except (TypeError, ValueError):
        pm = None

    try:
        ph = float(company.get("Promoter Holding"))
    except (TypeError, ValueError):
        ph = None

    try:
        rev = float(company.get("Revenue"))
    except (TypeError, ValueError):
        rev = None

    # P/E Ratio (Max 25)
    if pe is not None:
        if pe <= 10:
            score += 25
        elif pe <= 15:
            score += 15
        elif pe <= 20:
            score += 5

    # Debt to Equity (Max 25)
    if de is not None:
        if de >= 20:
            score += 25
        elif de >= 10:
            score += 15
        elif de >= 5:
            score += 10

    # Profit Margin (Max 15)
    if pm is not None:
        if pm >= 20:
            score += 15
        elif pm >= 10:
            score += 10
        elif pm >= 5:
            score += 5

    # Promoter Holding (Max 20)
    if ph is not None:
        if ph >= 70:
            score += 20
        elif ph >= 50:
            score += 15
        elif ph >= 30:
            score += 10

    # Revenue (Max 15)
    if rev is not None:
        if rev >= 100000:
            score += 15
        elif rev >= 50000:
            score += 10
        elif rev >= 10000:
            score += 5

    return score

def test_single_company(ticker_symbol):
    entry = {"Company Name": ticker_symbol, "Ticker": ticker_symbol}
    print(f"[TEST] Fetching data for {ticker_symbol}")
    data = fetch_company_data(entry)
    if data:
        print(json.dumps(data, indent=2))
        score = calculate_score(data)
        print(f"✅ Score for {ticker_symbol}: {score}/100")
    else:
        print("❌ Data incomplete or unavailable")

def main():
    tickers = read_all_tickers()
    print(f"[INFO] Fetching data for {len(tickers)} companies...")

    results = []
    for entry in tickers:
        print(f"[INFO] Processing: {entry['Company Name']} ({entry['Ticker']})")
        data = fetch_company_data(entry)
        if data:
            score = calculate_score(data)
            data["Score"] = score
            results.append(data)
            print(f"   ✅ Included with Score: {score}")
        else:
            print("   ❌ Skipped due to missing data")

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"[DONE] Saved {len(results)} companies to {OUTPUT_JSON}")

    # Test one company manually
    test_single_company("RELIANCE.NS")  # Example: replace with another NSE ticker if needed

if __name__ == "__main__":
    main()