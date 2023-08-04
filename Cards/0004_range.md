
# Range

#Dispersion

## Theory

The **range** is the difference between the highest and lowest observed values.

## Recipe

Import the dependencies.

```python
import numpy as np
import pandas as pd
```

Load the sample data.

```python
X = pd.read_csv("../data/practicaltest.csv")["female"]
```

Return the sample range.

```python
np.ptp(X)
```
