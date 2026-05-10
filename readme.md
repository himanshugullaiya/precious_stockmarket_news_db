# NSE Corporate Events Intelligence Dashboard

![Dashboard](Working%20Images/Image%201.png)

![Filtering](Working%20Images/Image%202.png)

---

# The Core Insight

> **Financial media reports what companies tell journalists. This system captures what companies tell SEBI.**

Exchange filings are the primary source. Media coverage is the echo.

By the time a stock move gets covered in financial news, the setup is already priced in. The real edge lies in tracking corporate announcements directly at the source — order wins, joint ventures, capacity expansions, institutional activity — before the narrative reaches the broader market.

This is the gap this project was built to fill.

---

# About The Project

NSE Corporate Events Intelligence Dashboard is a Python + PostgreSQL + Streamlit based market intelligence system that parses NSE/SEBI exchange filings directly and makes them searchable, filterable, and actionable.

The system detects early-stage corporate developments including:

- Order wins
- Strategic tie-ups and joint ventures
- Mergers and acquisitions
- Government contract developments
- Capacity expansion announcements
- Investor and institutional activity
- Business expansion signals

The goal is to identify meaningful corporate catalysts **before the broader market fully reacts** — and use them to assess whether a price move has a real narrative backing it, or whether it is likely to fade.

---

# Why This Matters for Trading

A breakout without a narrative is noise. A breakout with a narrative is a setup worth studying.

This system serves two purposes:

**1. Pre-trade probability filter**
Before entering a setup, check whether there is a corporate filing backing the move. If volumes are building and there is a SEBI-disclosed event behind it — order win, JV, capacity addition — the probability that the move sustains increases significantly. Buyers are not absorbing liquidity blindly; there is a reason.

**2. Past move study engine**
Understanding how major stock moves develop requires studying the full arc: filing → narrative build → price action execution. This system makes that research fast and structured — search any company, filter by event type or date, and reconstruct exactly how the catalyst unfolded.

---

# Features

## Backend
- Automated NSE corporate event parsing
- ZIP download and extraction pipeline
- PostgreSQL database storage
- Duplicate removal system
- Historical event collection

## Frontend
- Company name and symbol search
- Keyword filtering
- Date range filtering
- Event type filtering
- One-click symbol copy to clipboard
- CSV export for further analysis

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

## Start frontend

```bash
streamlit run Frontend.py
```

---

# Roadmap

- LLM-based event scoring and importance ranking
- Automatic summarization of filing content
- Noise filtering — remove low-value routine disclosures
- Real-time filing updates
- TradingView chart integration
- Event backtesting — map filings to subsequent price moves
- Sector-wise event clustering
- Catalyst ranking engine by historical price impact

---

# Author

Built out of a genuine gap identified after years of studying Indian equity markets. Financial news covers what companies want the public to know. Exchange filings reveal what companies are required to disclose. This system works at that second layer.