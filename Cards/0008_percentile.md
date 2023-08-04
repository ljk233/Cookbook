
# *N*th percentile

#Position

## Theory

The ***n*th percentile** is the value *p* such that *n*% of the observations are less than *p*,  and (100 - *n*)% of the observations are greater than *p*.

## Recipe

Import the dependencies.

```python
import pandas as pd
```

Load the sample data.

```python
X = pd.read_csv("../data/practicaltest.csv")["total"]
```

Return *q*-0.05.

```python
X.quantile(0.05)
```
