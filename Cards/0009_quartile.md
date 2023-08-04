
# Quartiles

#Position

## Theory

The **quartiles** are the three values that separate a sample into four even parts.

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

Return the sample quartiles.

```python
X.quantile(np.linspace(0.25, 0.75, num=3)).rename("quartiles")
```
