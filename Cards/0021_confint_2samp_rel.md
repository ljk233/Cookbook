
# Confidence interval for the difference between two means (matched samples)

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
import statsmodels.api as sm
```

### Large samples

Load the data.

```python
survey = pd.read_parquet("../Data/survey.parquet")
```

There is a missing record where a student did not complete the question.
Drop this record.

```python
clean_survey = survey.dropna(subset="writing_hand_span")
```

Return an approximate difference between the writing and non-writing hand spans of students.

```python
sm.stats.zconfint(
     clean_survey["writing_hand_span"] - clean_survey["non_writing_hand_span"]
)
```

### Exact

Load the data.

```python
darwin = pd.read_parquet("../data/darwin.parquet")
```

Return a confidence interval for the difference between mean cross- and self-fertilised plant heights.

```python
sm.stats.DescrStatsW(darwin["cross"] - darwin["self"]).tconfint_mean()
```

## References

- *[Confidence Intervals for Matched Samples, Continuous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals6.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
