
# Range

*2023-08-03*

## Notes

The **range**:

- is a measure of dispersion for numeric data
- is the difference between the highest and lowest observed values
- is sensitive to outliers
- has the same units as the data

## Examples

Import the dependencies.

```python
import numpy as np
import pandas as pd
```

Load the data.

```python
practical_test = pd.read_parquet("../data/practicaltest.parquet")
```

Return the range of the total pass rate.

```python
practical_test["total"].max() - practical_test["total"].min()
```

Alternatively, we could use *NumPy*.

```python
np.ptp(practical_test["total"])
```
