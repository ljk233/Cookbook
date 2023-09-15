
# One sample test

*2023-09-15*

## Notes

Both results,

- rely on the central limit theorem
- use the estimated standard error of the mean
- have the same test statistic, but its interpretation may differ

For the *z*-test,

- underlying population distribution does not matter
- is valid for large sample (*n* ≥ 25)
- null distribution is the standard normal distribution

And for the *t*-test,

- underlying population distribution is assumed to be normal
- is valid for any population size
- null distribution is *t*(*n* - 1)

## Examples

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
```

### One sample *z*-test

Load the data.

```python
practical_test = pd.read_parquet("../data/practicaltest.parquet")
```

The hypotheses are,

H<sub>0</sub> : μ = 50%;
H<sub>1</sub> : μ ≠ 50%,

where μ is the mean total pass rate.

Return the result of the hypothesis test.

```python
# Returns Z, p-val
sm.stats.ztest(practical_test["total"], value=50)
```

### One sample *t*-test

Load the data.

```python
schoolgirl = pd.read_parquet("../data/schoolgirl.parquet")
```

Studies have found that the meanheight of 11 year-old girls is 144cm.
([onaverage.com](https://www.onaverage.co.uk/body-averages/average-child-height), 2023).

The hypotheses are,

H<sub>0</sub> : μ<sup>\*</sup> = 144cm;
H<sub>1</sub> : μ<sup>\*</sup> > 144cm,

where μ<sup>*</sup> is the mean height (in centimetres) of 11-year-old school girls.

Return the result of the hypothesis test.

```python
# Returns T, p-val, df
sm.stats.DescrStatsW(schoolgirl["height"]).ttest_mean(value=144, alternative="larger")
```

Alternatively, we can use *SciPy*.

```python
st.ttest_1samp(schoolgirl["height"], 144, alternative="greater")
```

## References

- *Testing hypotheses* (M248, 2019)
- *Hypothesis Testing* (Elementary Statistics, 2012)
