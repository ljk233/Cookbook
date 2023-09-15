
# Two sample test of the difference between two means (independent samples)

*2023-09-15*

## Notes

Both results,

- require that the samples are independent
- rely on the central limit theorem
- use the estimated standard error of the mean
- use the pooled sample deviation
- assume that there is a common variance
  - This is taken to mean that the ratio of the larger *S* to the smaller *S* is less than 3

For the *z*-test,

- the distributions of the underlying population do not matter
- both sample size *n*<sub>1</sub>, *n*<sub>2</sub> ≥ 25

For the *t*-test,

- the underlying population distribution should be normal, or at least approximately normal

Note, if one sample is considered to be small, then use the *t*-test.

## Examples

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
```

### Two sample *z*-test

Load the data.

```python
practical_test = pd.read_parquet("../Data/practicaltest.parquet")
```

The hypotheses are,

H<sub>0</sub> : μ<sub>M</sub> = μ<sub>F</sub>;
H<sub>1</sub> : μ<sub>M</sub> ≠ μ<sub>F</sub>,

where μ<sub>M</sub>, μ<sub>F</sub> are the mean pass rates for males and females, respectively.

Return the result of the hypothesis test.

```python
# Returns Z, p-val
sm.stats.ztest(practical_test["male"], practical_test["female"])
```

### Two sample *t*-test

Load the data.

```python
skull = pd.read_parquet("../Data/skull.parquet")
```

The hypotheses are,

H<sub>0</sub> : μ<sub>Etr</sub> = μ<sub>Ita</sub>;
H<sub>1</sub> : μ<sub>Etr</sub> ≠ μ<sub>Ita</sub>,

where μ<sub>Etr</sub>, μ<sub>Ita</sub> are the mean skull breadths of Etruscan and Italian skulls, sespectively.

Select Etruscan and modern Italian skulls.

```python
etruscan = skull.query("skull == 'etruscan'")["breadth"]
italian = skull.query("skull == 'italian'")["breadth"]
```

Return the result of the hypothesis test.

```python
# Returns T, p-val, df
sm.stats.CompareMeans.from_data(etruscan, italian).ttest_ind()
```

Alternatively, we can use *SciPy*.

```python
st.ttest_ind(etruscan, italian)
```

## References

- *Hypothesis Testing* (Elementary Statistics, 2012)
