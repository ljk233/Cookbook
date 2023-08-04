
# Deciles

#Position

## Theory

The **deciles** are the nine values that separate a sample into 10 even parts.

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

Return sample deciles.

```python
X.quantile(np.linspace(0.1, 0.9, num=9)).rename("deciles")
```
