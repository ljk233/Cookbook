
# *z*-score

*2023-08-04*

## Note

The ***z*-score**:

- is a measure of position
- measures the number of standard deviations an observation falls above or below the mean
- is a method of standardisation
- is scale-free

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
school_girl = pd.read_parquet("../data/schoolgirl.parquet")
```

Return the *z*-score for each height.

```{python}
st.zscore(school_girl["weight"], ddof=1).rename("z_weight")
```

Note, we pass `ddof=1` so the sample standard deviation is used, rather than the population standard deviation.

## References

- *Multivariate analysis* (M249, 2007)
  - I could not find a nice reference for the *z*-score in M248
  - This is not to say it is not addressed there, but it is not obvious
