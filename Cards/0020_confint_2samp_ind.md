
# Confidence interval for the difference between two means (independent samples)

*2023-09-15*

## Notes

Both results,

- require that the samples are independent
- rely on the central limit theorem
- use the estimated standard error of the mean
- use the pooled sample deviation
- assume that there is a common variance
  - This is taken to mean that the ratio of the larger *S* to the smaller *S* is less than 3

For large samples (*n* ≥ 25),

- the underlying population distributions does not matter
- use the standard normal distribution

And for small samples (*n* < 25),

- the underlying population distributions should be (at least approximately) normal
  - This can be checked with a normal probability plot
- use *t*(*n*<sub>1</sub> + *n*<sub>2</sub> - 1)

Note, if one sample is considered to be small, then consider them both to be small samples and use the *t*-distribution.

## Examples

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
```

### Large samples

Load the data.

```python
practical_test = pd.read_parquet("../Data/practicaltest.parquet")
```

Return an approximate 95%-confidence interval for the difference between male and female pass rates.

```python
sm.stats.zconfint(practical_test["male"], practical_test["female"])
```

### Exact

Load the data.

```python
skull = pd.read_parquet("../Data/skull.parquet")
```

Select Etruscan and modern Italian skulls.

```python
etruscan = skull.query("skull == 'etruscan'")["breadth"]
italian = skull.query("skull == 'italian'")["breadth"]
```

Return an exact 95%-confidence interval for the mean difference between the skull breadths.

```python
sm.stats.CompareMeans.from_data(etruscan, italian).tconfint_diff()
```

## References

- *Interval Estimation* (M248, 2019)
- *[Confidence Interval for Two Independent Samples, Continuous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals5.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
