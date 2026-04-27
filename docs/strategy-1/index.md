# Strategy 1 — Macro Bollinger Vol Target – Breakout

## What it does (plain language)

It tries to detect when a market is in a **Big crisis**, then enter after **early recovery signals**, and allocate capital to a set of liquid single stocks **only when they are breaking out to new recent highs**.

Analogy: it’s like waiting for a storm (crisis), then investing once the weather starts clearing—*but only in the boats already moving fastest (breakouts)*. A Country does never break.

## Key concepts

- **Bollinger Bands:** a moving average plus/minus a multiple of recent volatility.
- **Breakout:** price reaching the highest level of the last *N* days.
- **Volatility targeting (here):** weight stocks by **inverse recent volatility** (less volatile → larger weight), then cap per-name weight.
- **Turnover:** total *dollars traded per day* (price × volume), used as a liquidity proxy. For example, if a stock trades 100,000 shares in a day at $5 each, its turnover is 500,000.
- **ROC (Rate of Change):** the percentage change over a lookback window.
    - In this strategy, `roc_momentum` is computed over `roc_momentum_lookback`, and then converted into a **z-score** (`roc`) using a rolling mean/std over `roc_distribution_window`.
    - Intuition: it measures whether the recent move is *unusually negative* compared to recent history (used to detect “crisis” conditions).
- **SMA (Simple Moving Average):** the average of the last *N* closing prices.
    - Here, `sma_trade` acts as a trend filter and a control signal (via SMA cross events).
- **Mean reversion:** the idea that after an extreme move, price often “snaps back” toward a typical level.
    - In this strategy, the “crisis” + recovery entry is a mean-reversion-style component (entering as the market recovers from being extremely oversold).
- **Trend following:** the idea of participating when price shows sustained strength (and exiting on weakness).
    - In this strategy, the **breakout filter** on single names and the moving-average / Bollinger mean control behave like trend-following components.

Continue:

- [How it works (technical)](how-it-works.md)
- [Data requirements](data-requirements.md)
- [How to run](how-to-run.md)
