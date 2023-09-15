
# Two sample test of the difference between two means (matched pairs)

*2023-09-15*

## Notes

- Samples are dependent
- If the sample size *n* < 25, then the distribution of the underlying population must be at least approximately normally distributed
- Because the data are matched, we can use the difference between pairs of observations
  - So for example, *D* = *X* - *Y*
  - This dimension reduction means the estimated standard error is *S*<sub>*D*</sub>

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
darwin = pd.read_parquet("../data/darwin.parquet")
```

The hypotheses are,

H<sub>0</sub> : μ<sub>D</sub> = 0;
H<sub>1</sub> : μ<sub>D</sub> ≠ 0,

where μ<sub>D</sub> = μ<sub>X</sub> - μ<sub>S</sub>, and μ<sub>X</sub>, μ<sub>S</sub> are the mean heights of cross- and self-fertilised plants, respectively.

Return the result of the hypothesis test.

```python
st.ttest_rel(darwin["cross"], darwin["self"])
```

Alternatively, we can use a one-sample *t*-test to return the same result.

```python
st.ttest_1samp(darwin["cross"] - darwin["self"], popmean=0)
```

## References

- *Computer Book B* (M248, 2019)
- *Hypothesis Testing* (Elementary Statistics, 2012)
