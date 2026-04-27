# Dependencies / `requirements.txt` (derived from imports)

There is no pinned dependency file in the repo. Based on **Python + notebook imports**, a practical `requirements.txt` is:

```txt
# Core
numpy
pandas
pymongo
python-dateutil

# Bloomberg data access (requires Bloomberg + blpapi installed)
xbbg

# Common analytics used elsewhere in repo / notebooks
matplotlib
scipy
scikit-learn
jupyter
openpyxl

# Optional (only if you use those notebooks/modules)
backtesting
pdblp
TA-Lib
# bql  (Bloomberg BQL python package; availability depends on your environment)
```

Install:

```powershell
pip install -r requirements.txt
```
