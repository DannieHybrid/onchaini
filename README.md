# On-Chain Intelligence Terminal

A real-time blockchain intelligence system that detects whale activity, smart money flows, and exchange-level capital movements on Ethereum.

---

## What it does

- Ingests Ethereum blocks via JSON-RPC
- Parses and classifies transactions
- Detects whale and smart money wallets
- Tracks exchange inflows and outflows
- Generates market intelligence signals
- Visualizes insights in a real-time dashboard

---

## Architecture

Ingestion (RPC) → Transaction Parser → Intelligence Engine → Storage → Dashboard UI

---

## Tech Stack

- Python (data ingestion + analytics)
- Web3.py (Ethereum RPC interaction)
- Next.js (dashboard UI)
- TailwindCSS (UI styling)
- SQLite (local storage)

---

## How to run

### Backend

```bash
PYTHONPATH=. python scripts/run_intelligence.py
PYTHONPATH=. python scripts/run_history.py
PYTHONPATH=. python scripts/run_exchange_flows.py
Frontend
cd dashboard
npm install
npm run dev
Signals Generated
Whale accumulation detection
Smart money tracking
Exchange flow monitoring
Historical wallet behavior scoring
Purpose

This project simulates institutional-grade on-chain intelligence by reconstructing wallet behavior and capital flows directly from raw blockchain data.
```
