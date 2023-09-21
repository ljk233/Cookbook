
# Time series analysis: Decomposing non-seasonal time series

*2023-09-20*

A cheat sheet for decomposing a non-seasonal time series.

## Main

Import the dependencies.

```python
import pandas as pd
import statsmodels.tsa.api as tsa
import seaborn as sns
from matplotlib import pyplot as plt
```

Set the graphing theme.

```python
sns.set_theme()
```

Load and prepare the data.

```python
securities = pd.read_parquet("../Data/securities.parquet")
```

Plot the time series.

```python
securities.pipe(sns.relplot, x="date", y="yield", kind="line")
plt.ylim(bottom=0)
```

Decompose the time series by taking the simple moving average of order 9.

```python
decomp_securities = securities.rolling(window=9, center=True).mean().dropna()
```

Plot the fitted time series.

```python
decomp_securities.pipe(sns.relplot, x="date", y="yield", kind="line")
plt.ylim(bottom=0)
```
