# Data requirements (MongoDB)

At minimum:

- A DB for index history (notebook uses `backtest_crisis`) with collections named like the aliases in `portfolio.py` (e.g., `spx`, `dax`, etc.).
- A DB for turnovers (notebook uses `single_names`) with documents containing `ticker`, `date`, `turnover`.
- A DB `backtest_single_names` with collections per Bloomberg ticker (e.g., `SYDB DC Equity`) containing `Date` and `Close`.
