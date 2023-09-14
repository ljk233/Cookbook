
# Median

*2023-08-03*

## Note

The **median**:

- is a measure of central tendency for numeric data
- is the value that minimises the sum of absolute deviations
- is resistant to outliers
- is the 50th percentile
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

Return the median height of the school girls.

```python
school_girl["height"].median()
```

## References

- *Exploring and interpreting data* (M248, 2019)
