
# Time series analysis: Decomposing seasonal time series

*2023-09-20*

A cheat sheet for decomposing a seasonal time series.

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
# securities = pd.read_parquet("../Data/securities.parquet")
monthly_temp = pd.read_csv(
    "../Data/temperature_monthly.csv",
    index_col=0,
    date_format="%b-%Y"
)
monthly_temp.info()
```

Plot the time series.

```python
monthly_temp.pipe(sns.relplot, x="date", y="temperature", kind="line")
```

Decompose the time series.

```python
decomp_monthly_temp = tsa.seasonal_decompose(
    monthly_temp, model="additive", two_sided=True
)
```

Return the seasonal component.

```python
pd.Series(
   data=decomp_monthly_temp.seasonal.values[:12],
   name='seasonal factor',
   index=pd.RangeIndex(1, 13, name="period"),
)
```

Obtain and plot the seasonally adjusted series.

```python
# Collect the seasonally adjusted series
seasonal_adjusted = (
    (decomp_monthly_temp.observed - decomp_monthly_temp.seasonal)
    .rename("temperature")
    .to_frame()
)
# Plot the time series
seasonal_adjusted.pipe(sns.relplot, x="date", y="temperature", kind="line")
plt.ylim(bottom=0)
```

Obtain and plot the trend component.

```python
# Obtain the trend component
trend = seasonal_adjusted.rolling(35, center=True).mean()
# Plot the trend component
trend.pipe(sns.relplot, x="date", y="temperature", kind="line")
plt.ylim(bottom=0)
```

Obtain and plot the irregular component.

```python
# Obtain the irregular component
irreg = seasonal_adjusted - trend
# Plot the irregular component
irreg.pipe(sns.relplot, x="date", y="temperature", kind="line")
```

Plot the trend, seasonal factors, and irregular components in a single plot.

```python
f = decomp_monthly_temp.plot()
```
