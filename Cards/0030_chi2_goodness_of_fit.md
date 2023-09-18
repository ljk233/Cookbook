
# Chi-square goodness-of-fit test

*2023-09-15*

## Notes

The **chi-square test goodness-of-fit test**:

- is used to test if a sample of data came from a population with a specific distribution
- can be applied to any univariate discrete distribution for the cumulative distribution function can be found
  - We must be able to calculate the expectation
- test statistic χ<sup>2</sup> is taken from χ<sup>2</sup>(*k* - *r* - 1), where,
  - *k* is the distinct number of classes or categories
  - *r* is the number of parameters of the fitted distribution
- requires all expected counts to be greater than or equal to 5
  - If they aren't, the data will need to be binned

## Examples

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

The month of death of 82 descendents of Queen Victoria who died of natural causes were collected.

We will test the null hypothesis that a discrete uniform distribution is an adequate model for the data.

Load the data.

```python
royal_deaths = pd.read_parquet("../data/royaldeath.parquet")
```

Return the result of the hypothesis test.

```python
st.chisquare(royal_deaths["n_deaths"])
```

## References

- *Non-parametric and goodness-of-fit tests* (M248, 2019)
- *[Chi-Square Goodness-of-Fit Test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm)* (National Institute of Standards and Technology, 2012)
