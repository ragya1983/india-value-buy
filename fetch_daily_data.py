import pandas as pd
import yfinance as yf
from datetime import datetime

# Load your list of companies (assumed to have a 'symbol' column)
df = pd.read_csv("final_filtered_companies.csv")
tickers = df['symbol'].dropna().unique().tolist()

results = []

for symbol in tickers:
    try:
        stock = yf.Ticker(symbol)
        fin = stock.info

        debt_equity = fin.get('debtToEquity')
        profit_margin = fin.get('profitMargins')

        if debt_equity is None or profit_margin is None:
            continue  # Skip companies with missing data

        # Score Logic
        score = 100
        if debt_equity > 1.5:
            score -= 50
        if profit_margin < 0.05:
            score -= 50

        results.append({
            'symbol': symbol,
            'debt_to_equity': debt_equity,
            'profit_margin': profit_margin,
            'score': score,
            'fetched_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
    except Exception as e:
        print(f"Error for {symbol}: {e}")

# Save results
out_df = pd.DataFrame(results)
out_df.to_csv("daily_scores.csv", index=False)
print("✅ Data fetched and saved to daily_scores.csv")
