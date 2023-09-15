
# Quartiles

*2023-08-04*

## Notes

The **quartiles**:

- are measures of position
- are the three values that separate a sample into four parts of approximately equal size
- are resistant to outliers
- have the same units as the data

## Example

Import the dependencies.

```python
import pandas as pd
```

Load the data.

```python
practical_test = pd.read_parquet("../data/practicaltest.parquet")
```

Return the quartiles of the female pass rate.

```python
practical_test["female"].quantile([0.25, 0.5, 0.75]).rename("quartiles")
```

## References

- *Exploring and interpreting data* (M248, 2019)
