
# Estimated standard error of the mean

*2023-09-14*

## Note

The **estimated standard error of the mean**:

- is the standard deviation of the sampling distribution of mean
- is a measure of the variability of the sampling distribution
- indicates how far sample means are likely to fall from the population mean
- uses the sample standard deviation, rather than the population standard deviation

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
practical_test = pd.read_parquet("../data/practicaltest.parquet")
```

Return the estimated standard error of the mean male pass rate.

```python
st.sem(practical_test["male"])
```

## References

- *Interval Estimation* (M248, 2019)
- *[Standard Error of the Mean (SEM)](https://statisticsbyjim.com/hypothesis-testing/standard-error-mean/)* (Statistics by Jim, 2023)
