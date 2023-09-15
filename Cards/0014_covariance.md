
## Notes

The **covariance**:

- is a measure of how much two random variables vary together
- measures of the direction of the relationship (positive or negative)
- does not measures the strength of relationship
  - This is in part because the measure is not scale-free, but instead is influenced by the choice of units
- will equal 0, if *X*, *Y* are independent random variables
  - However, the converse is not true
  - That is, we cannot say that because if *Cov*(*X*, *Y*) = 0, then *X*, *Y* are independent variables

Note, the covariance is included for coverage.
It is not particularly useful on its own, instead the correlation should be reported.

## Example

Import the dependencies.

```python
import pandas as pd
```

Load the data.

```python
practical_test = pd.read_parquet("../data/practicaltest.parquet")
```

Return the covariance between the male and female pass rates.

```python
practical_test[["male", "female"]].cov()
```

## References

- *Introductory unit* (M249, 2007)
- *Covariance* (The Concise Encyclopedia of Statistics, 2008)
