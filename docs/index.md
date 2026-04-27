# Live Trading Strategies (Windows) — Documentation

This document explains the **live trading strategies** area of this repository, with the current scope limited to **Strategy 1: Macro Bollinger Vol Target – Breakout**.

> Technical Note: In this codebase, “live strategy” largely means **signal generation + position sizing + portfolio weights** (often run from notebooks). I do not see a full broker/order-routing layer in the repository.

## What’s included / known gaps

**Included (from code):** strategy logic, parameters, data flow (MongoDB), Bloomberg data ingestion utilities (`xbbg`), and how the Strategy 1 backtest notebook runs end-to-end.

**LACKING:** VPN details (vendor, URLs), remote hostnames/IPs, MongoDB credentials/topology, Bloomberg API installation/licensing steps, and real order execution process.

## Where to go next

- [Repository map](repository/index.md) — folder layout and high-level diagrams
- [Setup](setup/index.md) — Windows / Python / venv / dependencies
- [Infrastructure](infrastructure/index.md) — VPN, MongoDB, Studio 3T
- [Strategy 1](strategy-1/index.md) — concepts, internals, how to run
- [Glossary](glossary.md)
