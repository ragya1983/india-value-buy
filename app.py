from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logic")
def logic():
    return render_template("logic.html")


# New route for /explore
@app.route("/explore")
def explore():
    try:
        with open("final_cleaned_data.json", "r") as f:
            companies = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return "Error loading company data", 500

    # Get selected sector from query parameter
    selected_sector = request.args.get("sector")

    if selected_sector:
        filtered_companies = [c for c in companies if c.get("Sector") == selected_sector]
        top_companies = sorted(filtered_companies, key=lambda x: x.get("Score", 0), reverse=True)[:10]
    else:
        top_companies = sorted(companies, key=lambda x: x.get("Score", 0), reverse=True)[:10]

    # Create a list of unique sectors
    sectors = sorted(list(set(c.get("Sector", "Unknown") for c in companies)))

    return render_template("explore.html", top_companies=top_companies, sectors=sectors, selected_sector=selected_sector)

import json

@app.route("/company/<ticker>")
def company_detail(ticker):
    with open("final_cleaned_data.json", "r") as f:
        companies = json.load(f)
    
    # Find the matching company
    company = next((c for c in companies if c["Ticker"].lower() == ticker.lower()), None)

    if not company:
        return render_template("not_found.html", ticker=ticker), 404

    return render_template("search.html", company=company)

# New route for search redirection
@app.route("/search")
def search_redirect():
    ticker = request.args.get("ticker")
    if ticker:
        return redirect(url_for('company_detail', ticker=ticker))
    return render_template("not_found.html", ticker="Unknown"), 400

if __name__ == "__main__":
    app.run(debug=True)