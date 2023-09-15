
# Pearson correlation coefficient

*2023-09-15*

## Notes

The **Pearson correlation coefficient *r***:

- is a measure of the strength and direction of a linear association between two quantitative variables
  - The sign indicates the direction, and the magnitude the strength
- has a range [-1, 1]
- assumes that the pair of variables have a joint normal distribution
  - This means that given any specific value of *x*, the *y* values are normally distributed; and vice-versa
- is not sensitive to the choice of unit
- is scale-free

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
practical_test = pd.read_parquet("../Data/practicaltest.parquet")
```

Return the correlation between the male and female pass rates.

```python
practical_test[["male", "female"]].corr()
```

Alteratively, we could use *SciPy* to return a more complete result.

```python
st.pearsonr(practical_test["male"], practical_test["female"])
```

## References

- *Introductory unit* and *Multivariate analysis* (M249, 2007)
- *Correlation and Regression* (Elementary Statistics, 2012)
