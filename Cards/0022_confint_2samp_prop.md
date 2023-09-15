# Confidence interval for the difference between two proportions

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

Return an approximate 95%-confidence interval for the difference between the proportion of males and females still living at home with their parents.

```python
sm.stats.confint_proportions_2indep(32, 86, 20, 64)
```

## References

- *Interval Estimation* (M248, 2019)
- *[Confidence Interval for Two Independent Samples, Dichotomous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals7.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
