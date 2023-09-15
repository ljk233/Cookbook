
# One sample test of a proportion

*2023-09-15*

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

The hypotheses are,

H<sub>0</sub> : p = 0.5;
H<sub>1</sub> : p > 0.5,

where *p* is the proportion of voters who support the candidate.

Return the results of the hypothesis test.

```python
# Returns Z, p-val
sm.stats.proportions_ztest(260, 500, value=0.5, alternative="larger")
```

## References

- *Testing hypotheses* (M248, 2019)
- *Hypothesis Testing* (Elementary Statistics, 2012)
