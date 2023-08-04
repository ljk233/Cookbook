
# *Q-Q* plot

#Position

## Theory

The ***Q-Q* plot**, or *quantile-to-quantile* plot, is a graph that tests the conformity between the empirical distribution and the given theoretical distribution.

## Recipe

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
from matplotlib import pyplot as plt
```

Load the sample data.

```python
X = pd.read_csv("../data/practicaltest.csv")["female"]
```

Plot the *Q-Q* plot.

```python
res = st.probplot(X, plot=plt)
```
