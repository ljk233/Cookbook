
# Quintiles

#Position

## Theory

The **quintiles** are the four values that separate a sample into five even parts.

## Recipe

Import the dependencies.

```python
import numpy as np
import pandas as pd
```

Load the sample data.

```python
X = pd.read_csv("../data/schoolgirl.csv")["height"]
```

Return sample quintiles.

```python
X.quantile(np.linspace(0.2, 0.8, num=4)).rename("quintiles")
```
