# MongoDB (database)

MongoDB is used as the project’s **time-series data store**.

- Index/country price history is read by `Base.fetch_data_db()` in `...\base.py`.
- Single-name price history is stored/read from the `backtest_single_names` database in `single_names_sizing.py`.

> Technical Note: Most code assumes `localhost:27017`. Collections generally contain a `Date` field and OHLCV-like fields (at minimum `Close`).
