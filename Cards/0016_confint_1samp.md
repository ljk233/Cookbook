
# One sample confidence interval for the mean

*2023-09-14*

## Notes

Both results,

- rely on the central limit theorem
- use the estimated standard error of the mean

For large samples (*n* ≥ 25),

- the underlying population distribution does not matter
- use the standard normal distribution

And for small samples (*n* < 25),

- the underlying population distribution should be (at least approximately) normal
  - This can be checked with a normal probability plot
- use *t*(*n* - 1)

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
X = pd.read_parquet("../data/schoolgirl.parquet")["height"]
```

Return an approximate 95%-confidence interval for the mean height of the school girls.

```python
sm.stats.zconfint(X)
```

Alternatively, we can use *SciPy*.

```python
st.norm.interval(0.95, X.mean(), st.sem(X))
```

### Small samples

Load the data.

```python
Y = pd.read_parquet("../data/darwin.parquet")["self"]
```

Return an exact 95%-confidence interval for the mean height of self-fertilised plants.

```python
sm.stats.DescrStatsW(Y).tconfint_mean()
```

Alternatively, we can use *SciPy*.

```python
st.t.interval(0.95, Y.shape[0] - 1, Y.mean(), st.sem(Y))
```

## References

- *Interval Estimation* (M248, 2019)
- *[Confidence Intervals for One Sample: Continuous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals3.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
