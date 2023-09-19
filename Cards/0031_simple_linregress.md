
# Simple linear regression

*2023-09-15*

A cheatsheet for performing a simple linear regression analysis.

## Main

Import the dependencies

```python
import numpy as np
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt
```

Set the graphing default.

```python
sns.set_theme()
```

Load the data.

```python
cholesterol = pd.read_parquet("../data/cholesterol.parquet")
```

### Pre-fitting

Plot the data.

```python
cholesterol.pipe(sns.relplot, x="age", y="cholesterol")
```

Report the Pearson correlation coefficient *r*.

```python
st.pearsonr(cholesterol["age"], cholesterol["cholesterol"])
```

### Fit the model

Model and fit the data.

```python
model = sm.OLS.from_formula("cholesterol ~ age", data=cholesterol)
result = model.fit()
```

Summarise the fitted model.

```python
print(result.summary(slim=True))
```

Report the regression coefficent β.

```python
result.params.rename("coef").to_frame().assign(
    lcb=result.conf_int(0.05)[0],
    ucb=result.conf_int(0.05)[1],
)
```

### Test the model

Test the null hypothesis β = 0.

```python
result.tvalues.rename("t").to_frame().assign(pval=result.pvalues).round(4)
```

### Check the model assumptions

Residual plot showing residual against fitted value.

```python
plt.scatter(result.fittedvalues, result.resid)
plt.axhline(y=0, lw=2, ls="--", color="r")
plt.ylabel("Residual")
plt.xlabel("Fitted value")
```

Normal probability plot using the residual values.

```python
_ = st.probplot(result.resid, plot=plt)
```

### Prediction

Return a point and prediction interval.

```python
result.get_prediction({"age": 35}).summary_frame()
```

## References

- *Regression* (M248, 2019)
- *Introduction to statistical modelling and R* (M348, 2022)
