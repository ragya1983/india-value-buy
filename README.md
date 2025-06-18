# 🏢 Buy Indian Companies — CS50 Final Project

A web app to discover undervalued Indian companies that might be worth acquiring. This project was built for Harvard’s CS50 final project.

---

- Filters 1100+ Indian listed companies based on financial stress
- Uses five financial metrics: **P/E Ratio**, **Debt-to-Equity**, **Profit Margin**, **Interest Coverage**, and **Revenue**
- Assigns a score from 0–100 based on a weighted formula that detects undervaluation or distress
- Lets you explore by sector or search any company by name or ticker
- Fetches live financial data such as market capitalization and stock prices from the [Yahoo Finance API](https://pypi.org/project/yfinance/)

---

## 🧠 How the Score Works

The score is computed from five financial metrics using weighted rules:

- Low P/E Ratio results in a higher score
- High Debt-to-Equity ratio results in a higher score (as it can be attractive for buyouts)
- Positive Profit Margin adds bonus points
- High Interest Coverage adds bonus points
- High Revenue adds bonus points

The idea is to suggest companies that might be attractive for acquisition or investment based on financial indicators.

---

## 📊 Data Sources and Methodology

- The list of companies was taken from the National Stock Exchange (NSE) of India.
- Live financial data like market capitalization and stock prices are fetched from Yahoo Finance using its public API.
- We filter and retain only companies that have complete data available for all the selected financial metrics.
- The data and scores are computed to identify potentially undervalued or financially stressed companies.
- In real-world applications, this data should be dynamically updated via automated jobs or cron.
- For this project, to keep costs zero and hosting free, automatic periodic updates via cron jobs were not implemented; data updates are done manually.

---

## 🛠 Tech Stack

- Python + Flask
- HTML, CSS (custom + inline)
- JSON (for static data storage)
- Yahoo Finance API (live financial data fetch)

---

## 🌐 Hosted On

This site is deployed on [Render](https://render.com).  
Live URL: [https://buy-indian-companies.onrender.com](https://buy-indian-companies.onrender.com)

---

## 🚀 To Run Locally

1. Clone this repository
2. Install dependencies:
   ```
   pip install flask yfinance
   ```
3. Start the app:
   ```
   python app.py
   ```
4. Open in browser:
   ```
   http://127.0.0.1:5000
   ```
5. **Update data periodically by running your update script manually** (e.g., `python daily_update.py`) to refresh the JSON data used by the app.

---

## 📌 Future Plans

- Automatic daily updates via cron job
- More financial metrics: Revenue trends, promoter holdings, etc.
- Public search and bookmarking features
- Company detail pages with summary analysis and Yahoo Finance links
- Sector-wise filtering and improved user interface

---

_This is a learning project. All data is for demonstration only. Please do not use it for real investment decisions._

Built with ❤️ as part of [CS50x](https://cs50.harvard.edu/x) 2025.