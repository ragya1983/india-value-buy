# India Value Buy — CS50 Final Project

#### Video Demo: https://youtu.be/kyTBSUpvvvE

#### Live Website: https://india-value-buy.onrender.com/

## Acknowledgments

I would like to acknowledge the assistance of ChatGPT in developing this project. Its guidance and support helped streamline coding, debugging, and documentation processes.

---

## Description

India Value Buy is a web application designed to help users discover undervalued or financially distressed Indian companies that might be attractive acquisition or investment targets. Built as part of Harvard’s CS50 final project, it demonstrates practical use of financial data analysis, web development with Flask, and data visualization.

The project filters over 1,100 Indian listed companies based on key financial indicators including P/E Ratio, Debt-to-Equity ratio, Profit Margin, Interest Coverage, and Revenue. Using a weighted scoring system, it highlights companies showing potential for value investment or turnaround opportunities. Users can explore companies by sector or search by company name or ticker symbol.

Financial data sources include the National Stock Exchange of India (NSE) for the company list and Yahoo Finance for live market data such as market capitalization and stock prices. To keep hosting costs minimal, data updates are manual, but the architecture supports future automation via scheduled tasks.


---

## Project Structure and Key Files

- **app.py**: Main Flask app handling routing and rendering templates.
- **templates/**: HTML templates defining the website pages.
- **static/**: Static assets like CSS stylesheets.
- final_cleaned_data.json**: Static JSON storing financial data and computed scores.
- **requirements.txt**: Python dependencies including Flask and yfinance.
- **daily_update.py**: Script to manually fetch and update financial data from Yahoo Finance.
- **README.md**: This documentation file.

---

## How the Scoring Works

The score combines five financial metrics:

- **P/E Ratio**: Lower P/E leads to a higher score, indicating undervaluation.
- **Debt-to-Equity Ratio**: Higher debt can increase the score, signaling possible buyout opportunities.
- **Profit Margin**: Positive margins add to attractiveness.
- **Interest Coverage**: Higher ability to service debt adds points.
- **Revenue**: Strong revenue positively influences the score.

This scoring helps identify financially stressed but potentially valuable companies for further research.

---

## Design Choices

- **Manual Updates**: Automated daily updates were not implemented due to free hosting constraints on Render.com.
- **Static JSON Data**: Chosen for simplicity and cost-effectiveness, trading off real-time data freshness.
- **Clean UI**: Focus on usability with options to explore by sector or search directly.
- **Educational Purpose**: Scores do not constitute investment advice but illustrate data-driven filtering.

---

## Running Locally

1. Clone the repo:
   ```
   git clone https://github.com/yourusername/yourrepo.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open browser:
   ```
   http://127.0.0.1:5000
   ```
5. Update data manually:
   ```
   python daily_update.py
   ```

---

## Future Plans

- Automated updates with cron jobs
- Additional financial metrics and richer company profiles
- Enhanced UI with bookmarking and filtering features
- Improved data accuracy and completeness

---

## Disclaimer

This is an educational prototype. Use it only for learning, not for real financial decisions.

---

Built with ❤️ as part of [CS50x 2025](https://cs50.harvard.edu/x).

---
