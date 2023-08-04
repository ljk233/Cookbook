
# Sample standard deviation

#Dispersion 

## Theory

The **sample standard deviation** is the positive square root of the *sample variance*.

## Recipe

Import the dependencies.

```python
import pandas as pd
```

Load the sample data.

```python
X = pd.read_csv("../data/schoolgirl.csv")["height"]
```

Return the sample standard deviation.

```python
X.std(ddof=1)
```
