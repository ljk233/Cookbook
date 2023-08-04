
# Sample variance

#Dispersion 

## Theory

The **sample variance** is the average squared difference of the scores from the *mean*.

## Recipe

Load the dependencies.

```python
import pandas as pd
```

Get things ready.

```python
X = pd.read_csv("../data/schoolgirl.csv")["height"]
```

Return the sample variance.

```python
X.var(ddof=1)
```
