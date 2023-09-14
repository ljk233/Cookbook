
# Quantile

*2023-08-04*

## Note

The **α-quantile**:

- is a measure of position
- is the value *q* such that
  - 100 α % of the observations are less than *q*
  - 100(1 - α) % of the observations are greater than *q*
- has the same unit as the data

## Example

Import the dependencies.

```python
import pandas as pd
```

Load the data.

```python
school_girl = pd.read_parquet("../data/schoolgirl.parquet")
```

Return *q*-0.25 of the height of the school girls.

```python
school_girl["height"].quantile(0.25)
```

## References

- *Events occuring at random and population quantiles* (M248, 2019)
