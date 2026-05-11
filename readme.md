# NSE Corporate Events Intelligence Dashboard

> **Financial media reports what companies tell journalists. This system captures what companies tell SEBI.**

---

## Result: JAINREC — 35% in 8 Days

![JAINREC Case Study — Filing flagged on 2026-04-28, stock moved 35% in 8 days](Working%20Images/Image%201.png)

Shareholders meeting filing flagged on **2026-04-28**. Stock moved **35% in the following 8 days** — starting exactly from that date. The filing was visible here before the broader market reacted.

---

## Today's Dashboard — Live Filings

![Today's Results — 46 filings including mergers, order wins, credit ratings](Working%20Images/Image%202.png)

Search across all NSE filings by keyword — mergers, order wins, credit ratings, acquisitions — filtered by date and event type. **46 results on a single day.**

---

## What It Does

Parses NSE/SEBI corporate filings directly — before media covers them. Tracks order wins, JVs, mergers, acquisitions, capacity expansions, institutional activity.

Two use cases: **pre-trade catalyst check** and **studying how past moves built from filing → narrative → price action.**

---

## Tech Stack

Python · PostgreSQL · Streamlit · Pandas · psycopg2

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run Frontend.py
```

---

## Roadmap

LLM event scoring · filing summarization · noise filtering · real-time updates · TradingView integration · event backtesting

---

[GitHub](https://github.com/himanshugullaiya/precious_stockmarket_news_db)
