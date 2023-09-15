
# One sample confidence interval for a Poisson parameter

*2023-09-14*

## Notes

- Confidence interval is valid when *n*λ ≥ 30
  - In other words, at least 30 events are observed

## Example

Load the dependencies.

```python
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
```

At the 2022 FIFA World Cup, there were 172 goals scored in 64 matches, for an average of 2.69 goals per match.
Return an approximate 95%-confidence interval for the total number of goals scored per game.

```python
sm.stats.confint_poisson(172, 64, method="wald", alpha=0.05)
```

## References

- *Interval Estimation* (M248, 2019)
