
# Two sample test of the difference between proportions

*2023-09-15*

## Notes

- Samples are independent
- Each observation in both sammples is an independent Bernoulli trial
- All of *n*<sub>*X*</sub>*p*<sub>*X*</sub>, *n*<sub>*X*</sub>*q*<sub>*X*</sub> and *n*<sub>*Y*</sub>*p*<sub>*Y*</sub>, *n*<sub>*Y*</sub>*q*<sub>*Y*</sub> ≥ 5
  - This translates to there are at least 5 successes and at least 5 failures in each sample

## Example

Import the dependencies.

```python
import statsmodels.api as sm
```

A survey of 150 adults aged 25-34 found that 32 out of the 86 males questioned and 20 out of the 64 females questioned still lived at home with their parents.

The hypotheses are,

&ensp;&ensp;&ensp;&ensp;
H<sub>0</sub> : *p*<sub>M</sub> = *p*<sub>F</sub>;
H<sub>1</sub> : *p*<sub>M</sub> ≠ *p*<sub>F</sub>,

where *p*<sub>M</sub>, *p*<sub>F</sub> are the proportion of males and females aged between 25-34 still living at home with their parents, respectively.

Return the result of the hypothesis test.

```python
# Returns Z, p-val
sm.stats.test_proportions_2indep(
    32, 86, 20, 64, method="wald", compare="diff", return_results=False
)
```

## References

- *Interval Estimation* (M248, 2019)
