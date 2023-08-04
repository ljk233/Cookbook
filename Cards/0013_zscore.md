
# *z*-score

#Position

## Theory

The ***z*-score** is the number of standard deviations a value is away from the *sample mean*.

## Recipe

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the sample data.

```python
X = pd.read_csv("../data/practicaltest.csv")["total"]
```

Return sample deciles.

```python
pd.Series(st.zscore(X), name="zscore")
```
