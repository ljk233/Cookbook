
# One sample confidence interval for a proportion

*2023-09-14*

## Notes

- Each observation in the sample is an independent Bernoulli trial
- Both *np*, *nq* ≥ 5
  - This translates to there being at least 5 successes and 5 failures

## Example

Import the dependencies.

```python
import statsmodels.api as sm
```

A candidate in a two-person election commissions a poll to determine who is ahead.
The pollster randomly chooses 500 registered voters, and determines that 260 out of the 500 favour the candidate.

Return an approximate 95%-confidence interval for the proportion of voters who back the candidate.

```python
sm.stats.proportion_confint(260, 500)
```

## References

- *Interval Estimation* (M248, 2019)
- *[Confidence Interval for One Sample, Dichotomous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals4.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
