
# Multiple linear regression

*2023-09-11*

A cheatsheet for performing a multiple linear regression analysis on a dataset.

## Main

Import the dependencies

```python
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt
```

Set the graphing defaults.

```python
sns.set_theme()
```

Load the data.

```python
peru = pd.read_csv("../Data/peru.txt", sep="\t")
```

## Fit the model

Model and fit the data.
The model is,

&ensp;&ensp;&ensp;&ensp;
`Systol ~ Age + Years + Weight + Height + Chin + Forearm + Calf + Pulse + Diastol`

```python
resp = peru["Systol"]
expl = peru.drop(columns="Systol")
model = sm.OLS(resp, sm.add_constant(expl))
regr = model.fit()
```

Summarise the model.

```python
print(regr.summary(slim=True))
```

Report the regression coefficents.

```python
regr.params.rename("coef").to_frame().assign(
    lcb=regr.conf_int(0.05)[0],
    ucb=regr.conf_int(0.05)[1],
)
```

## Testing the model

### Testing the coefficients of regression

*Box 4*

Testing all regression coefficients simultaneously.

```python
pd.Series([regr.fvalue, regr.f_pvalue], index=["F", "pval"]).round(4).rename("F-Test")
```

Testing the regression coefficients individually.

```python
regr.tvalues.rename("t").to_frame().assign(pval=regr.pvalues).round(4)
```

### Measuring how well a model fits

*Boxes 21:24*

Return the total, explained, and residual sum of squares.

```python
pd.Series(
    {"TSS": regr.centered_tss, "ESS": regr.ess, "RSS": regr.ssr}, name="Sum of squares"
)
```

Return the *R*<sup>2</sup> statistic, the percentage of variation accounted.

```python
regr.rsquared
```

Return the adjusted *R*<sup>2</sup> statistic.

```python
regr.rsquared_adj
```

Report the Akaike information criterion (AIC).

```python
regr.aic
```

## Diagnostics

### Checking the residuals

*Boxes 7:9*

Plot the residual against fitted values.

```python
plt.scatter(regr.fittedvalues, regr.resid)
plt.axhline(y=0, lw=2, ls="--", color="r")
plt.ylabel("Residual")
plt.xlabel("Fitted value")
```

Plot a normal probability plot for the fitted values.

```python
_ = st.probplot(regr.fittedvalues, plot=plt)
```

### Leverage and influence

*Boxes 10:15*

Collect a description of the outlier influence.

```python
influence = regr.get_influence()
```

Return the leverage of each observation.

```python
influence.hat_matrix_diag
```

Plot the standardised residuals against leverage.

```python
plt.scatter(influence.hat_matrix_diag, st.zscore(regr.resid))
plt.axhline(y=0, lw=2, ls="--", color="r")
plt.xlabel("Leverage")
plt.ylabel("Standadised residual")
```

Plot the standardised residuals against influence.

```python
plt.scatter(influence.influence, st.zscore(regr.resid))
plt.axhline(y=0, lw=2, ls="--", color="r")
plt.xlabel("Influence")
plt.ylabel("Standadised residual")
```

Report the Cook's distance.

```python
influence.cooks_distance[0]
```

Plot the Cook's distance.

```python
plt.stem(expl.index, influence.cooks_distance[0])
```

## Prediction

```python
...
```

## Choosing the explanatory variables

### Multicollinearity

*Boxes 19:20*

Plot a scatterplot matrix.

```python
sns.pairplot(peru, height=1.5, corner=True)
```

Return the correlation matrix.

```python
peru.corr()
```

Plot a correlation heatmap.

```python
sns.heatmap(peru.corr(), cmap="bwr", center=0, vmin=-1)
```

## Performing stepwise regression

> Stepwise regression is a step-by-step iterative procedure in which a regression model is built at each step with a different selection of explanatory variables.
> The procedure continues by adding (or removing) potential explanatory variables in turn and calculating a selection criterion – for example, the *AIC* – to assess how the model fits at each step.
> Based on comparing the values of the selection criterion, the best model is finally determined.

*Box 25*

### Forward stepwise regression

```python
_resp = "Systol"
y = peru[_resp]
expl_cands = set(peru.columns)
expl_cands.discard(_resp)
expl_cands.add(None)
fselected_expl = []
all_res = []

while True:
    res = []
    for expl_cand in expl_cands:
        selected_cands = fselected_expl
        if expl_cand:
            selected_cands = selected_cands + [expl_cand]

        res.append(
            [expl_cand, sm.OLS(y, sm.add_constant(peru[selected_cands])).fit().aic]
        )
    all_res.append(sorted(res, key=lambda x: x[1], reverse=True))
    selected = sorted(res, key=lambda x: x[1], reverse=True).pop()[0]
    if not selected:
        break

    fselected_expl.append(selected)
    expl_cands.discard(selected)

print(fselected_expl)
all_res[3]
```

Fit the model using the selected explanatory variables and compare the models.

```python
fmodel = sm.OLS(y, sm.add_constant(expl[fselected_expl]))
fregr = fmodel.fit()
print(fregr.summary(slim=True))
```

### Backward stepwise regression

## References

- *Regression* (M248, 2019)
- *Multiple linear regression* (M348, 2022)
