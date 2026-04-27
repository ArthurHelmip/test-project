# How to run (and “test”) Strategy 1

1. Start MongoDB on the machine where you will run the notebook.
2. Open the notebook:
      - `live strategies\1. [macro bollinger] vol target - breakout\backtest.ipynb`
3. Run all cells.

Expected outputs:

- Per-country outputs and a combined portfolio series (written under folders like `individual output\...` and `combined output\...`).

> Technical Note: `data_update.py` references a module path `common\acute crisis` that is not present in this repo snapshot; you may need to run data updates in your standard environment where that module exists, or adapt the ingestion workflow.
