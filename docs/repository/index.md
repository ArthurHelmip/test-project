# Repository map (relevant)

- Strategy 1 folder:
    - `live strategies\1. [macro bollinger] vol target - breakout\strategy.py` (signals)
    - `...\single_names_sizing.py` (single-name selection + weights)
    - `...\position_sizing.py` (combine countries into a portfolio)
    - `...\portfolio.py` (list of country indices + configs)
    - `...\base.py` (MongoDB price-series loader)
    - `...\helper.py` (Mongo helpers + BBG single-name fetch/update)
    - `...\backtest.ipynb` (main runnable notebook)
- Data ingestion:
    - `data_update.py` (Bloomberg → MongoDB for index/aux series)

## High-level data flow

```mermaid
flowchart LR
    BBG[Bloomberg (xbbg / blp)] -->|bdh()| DU[data_update.py]
    DU -->|insert/update| MDB[(MongoDB)]

    MDB --> DBIDX[DB: backtest_crisis\nCollections: country/index series]
    MDB --> DBTO[DB: single_names\nCollection: turnovers (ticker,date,turnover)]
    MDB --> DBSN[DB: backtest_single_names\nCollections: 1 per BBG ticker]

    DBIDX --> ST[TrenderAcuteCrisisStrategy\n(strategy.py)]
    DBTO --> SN[single_names_sizing.py]
    DBSN --> SN

    ST --> SN
    SN --> PS[position_sizing.py\n(combine sleeves)]
    PS --> OUT[Outputs\nindividual output/\ncombined output/]
```

## Class diagram (Strategy 1)

```mermaid
classDiagram
    class Base {
        +symbol
        +db_name
        +start
        +end
        +data
        +fetch_data_db(db, collection, query, host, port)
        +get_data()
    }

    class TrenderAcuteCrisisStrategy {
        +get_data()
        +trade_signal_generator(...)
        +position_calculation(trade_signal)
        +series_return_calculation(...)
        +series_close_calculation(...)
    }

    Base <|-- TrenderAcuteCrisisStrategy
    TrenderAcuteCrisisStrategy ..> single_names_sizing : calls single_names_signal_return()
    TrenderAcuteCrisisStrategy ..> position_sizing : outputs per-country sleeve used in portfolio
```

## Sequence diagram (typical notebook run)

```mermaid
sequenceDiagram
    participant NB as backtest.ipynb
    participant DU as data_update.py
    participant MDB as MongoDB
    participant ST as strategy.py
    participant SN as single_names_sizing.py
    participant PS as position_sizing.py

    NB->>DU: update(asset_collection, backtest_crisis)
    DU->>MDB: write index/aux series
    NB->>ST: instantiate TrenderAcuteCrisisStrategy(...)
    ST->>MDB: read index price series (Base)
    ST->>SN: single_names_signal_return(...)
    SN->>MDB: read turnovers + single-name prices
    NB->>PS: create_combined_output(...)
    PS-->>NB: combined_output, weights, returns
```
