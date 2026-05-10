# Corporate Events Dashboard

![Dashboard](Working%20Images/Image%201.png)

![Filtering](Working%20Images/Image%202.png)

---

# About The Project

Corporate Events Dashboard is a Python + PostgreSQL + Streamlit based market intelligence system built to identify meaningful corporate developments before major price moves happen in the market.

Instead of relying on broad generalized financial news, this system focuses directly on company-level exchange filings and corporate announcements.

The goal is to detect:
- order wins
- strategic tie-ups
- joint ventures
- mergers
- government developments
- capacity expansion
- investor activity
- institutional signals
- business expansion

before the broader market fully reacts.

---

# Core Idea

> Important price moves are often preceded by subtle but meaningful corporate developments.

This project creates a searchable event intelligence layer over NSE corporate announcements.

In the future, LLMs will be integrated to:
- summarize filings
- rank importance of events
- remove low-value noise
- identify high-impact developments automatically

This creates a significantly more market-relevant information engine compared to traditional global news feeds which often have weak direct market correlation.

---

# Features

## Backend
- Automated NSE corporate event parsing
- ZIP download & extraction pipeline
- PostgreSQL database storage
- Duplicate removal system
- Historical event collection

---

## Frontend
- Company name search
- Symbol search
- Keyword filtering
- Date filtering
- Event type filtering
- Copy symbols directly to clipboard
- CSV export support

---

# Tech Stack

- Python
- PostgreSQL
- Streamlit
- Pandas
- psycopg2

---

# Run Locally

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start frontend

```bash
streamlit run Frontend.py
```

---

# Future Improvements

- LLM-based event scoring
- Event summarization
- Sentiment analysis
- Real-time updates
- TradingView integration
- Event backtesting
- Sector-wise clustering
- Catalyst ranking engine

---

# Author

Built as a personal market intelligence and event discovery system for trading research and catalyst analysis.