# Corporate Events Dashboard

A Python + PostgreSQL + Streamlit based market intelligence dashboard focused on identifying meaningful corporate events before major market moves.

---

## Project Overview

This system downloads and parses NSE corporate announcement data, stores it in PostgreSQL, and provides a fast searchable dashboard for traders/investors.

The core idea is:

> Important market moves are often preceded by subtle but meaningful corporate developments.

Examples:
- Order wins
- Capacity expansion
- Strategic tie-ups
- Joint ventures
- Government approvals
- Mergers
- Subsidiary incorporation
- Institutional activity
- Investor calls

Instead of relying on broad global news feeds with weak correlation, this system focuses directly on company-level events.

---

## Current Features

### Backend
- Automated NSE corporate event parsing
- ZIP extraction pipeline
- PostgreSQL storage
- Duplicate removal
- Date-wise data organization

### Frontend
- Company name search
- Symbol search
- Keyword filtering
- Date filtering
- Event type filtering (AN/BM)
- Copy filtered symbols directly to clipboard
- CSV export

---

## Tech Stack

- Python
- PostgreSQL
- Streamlit
- Pandas
- psycopg2

---

# Dashboard Preview

## Main Dashboard

![Dashboard](Working%20Images/Image%201.png)

---

## Search & Filtering System

![Filtering](Working%20Images/Image%202.png)

---

# Use Case

The primary use case is:

> To identify key corporate events before the actual market move happens.

The future roadmap is to integrate LLMs to:
- summarize filings
- rank event importance
- filter low-quality news
- detect meaningful catalysts automatically

This creates a much more market-relevant signal engine compared to traditional generalized news feeds.

---

# Future Improvements

- LLM-based event ranking
- Event importance scoring
- Sentiment classification
- Real-time updates
- TradingView integration
- Sector-wise event clustering
- Event backtesting against price moves

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

# Author

Built as a personal market intelligence and event discovery system for trading research.