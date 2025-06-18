# 🏢 Buy Indian Companies — CS50 Final Project

A web app to discover undervalued Indian companies that might be worth acquiring. This project was built for Harvard’s CS50 final project.

---

- Filters 1100+ Indian listed companies based on financial stress
- Uses five financial metrics: **P/E Ratio**, **Debt-to-Equity**, **Profit Margin**, **Interest Coverage**, and **Revenue**
- Assigns a score from 0–100 based on a weighted formula that detects undervaluation or distress
- Lets you explore by sector or search any company by name or ticker
- Live market cap data added via Yahoo Finance API

---

## 🧠 How the Score Works

- Score is computed from five metrics using weighted rules:
  - Low P/E Ratio → higher score
  - High Debt-to-Equity → higher score (attractive for buyouts)
  - Positive Profit Margin → bonus points
  - High Interest Coverage → bonus points
  - High Revenue → bonus points

Color code:
- 🔴 0–20: High distress
- 🟡 21–60: Moderate
- 🟢 61–100: Healthy

---

## 🛠 Tech Stack

- Python + Flask
- HTML, CSS (custom + inline)
- JSON (for static data)
- Yahoo Finance API (live data)

---

## 🌐 Hosted On

This site is deployed on [Render](https://render.com).  
Live URL: [https://buy-indian-companies.onrender.com](https://buy-indian-companies.onrender.com)

---

## 🚀 To Run Locally

1. Clone this repository
2. Install dependencies:  
   `pip install flask yfinance`
3. Start the app:  
   `python app.py`
4. Open in browser:  
   `http://127.0.0.1:5000`

---

## 📌 Future Plans

- Automatic daily updates via cron job
- More metrics: Revenue trends, promoter holding, etc.
- Public search and bookmarking
- Company detail pages with summary analysis and Yahoo Finance links
- Sector-wise filtering and improved UI

---

_This is a learning project. All data is for demonstration only. Please don’t use it for real investment decisions._

Built with ❤️ as part of [CS50x](https://cs50.harvard.edu/x) 2025.
