
# Median

#CentralTendency 

## Theory

The **median** is the value that minimises the sum of absolute deviations.
It is the *q*-0.5.

## Recipe

Import the dependencies.

```python
import pandas as pd
```

Load the sample data..

```python
X = pd.read_csv("../data/schoolgirl.csv")["height"]
```

Return the sample median.

```python
X.median()
```
