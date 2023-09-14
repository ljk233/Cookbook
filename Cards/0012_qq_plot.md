
# *Q-Q* plot

*2023-08-04*

## Note

The ***Q-Q* plot**, or *quantile-to-quantile* plot, is a graph that can be used to check the conformity between the empirical distribution and a given theoretical distribution.

## Recipe

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
from matplotlib import pyplot as plt
```

Load the sample data.

```python
X = pd.read_parquet("../data/practicaltest.parquet")["female"]
```

Plot a *Q-Q* plot.

```python
_ = st.probplot(X, plot=plt)
```

Note, the default is to check against the normal distribution.
A different theoretical distribution can be used by passing an argument for `dist`.
From the *SciPy* API reference,

> **dist** : *str or stats.distributions instance, optional*
>
> - Distribution or distribution function name.
> - The default is `‘norm’` for a normal probability plot.
> - Objects that look enough like a stats.distributions instance (i.e. they have a `ppf` method) are also accepted.
