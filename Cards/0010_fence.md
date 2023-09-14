
# Fences

*2023-08-04*

## Note

The upper and lower **fences** represent the cut-off values for upper and lower outliers.

## Recipe

Import the dependencies.

```python
import pandas as pd
```

Load the sample data.

```python
X = pd.read_csv("../data/practicaltest.csv")["male"]
```

Return the upper and lower sample fences.

```python
pd.Series(
    data={
        "lower": X.quantile(0.25) - 1.5 * st.iqr(X),
        "upper": X.quantile(0.75) + 1.5 * st.iqr(X),
    },
    name="fence",
)
```
