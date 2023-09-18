# Contingency tables

*2023-09-18*

Add note.

## Examples

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
from statsmodels.stats import api as sm
```

Load the data.

```python
survey = pd.read_parquet("../Data/survey.parquet").dropna(
    subset=["writing_hand", "arm_fold"]
).query("arm_fold != 'Neither'")
```

Cross-tabulate the data.

```python
xtab = pd.crosstab(survey["writing_hand"], survey["arm_fold"]).to_numpy()
```

Initialise a 2x2 contingency table.

```python
result = sm.Table2x2(xtab, shift_zeros=False)
```

Summarise the result.

```python
result.summary()
```

Return the relative risk.

```python
pd.Series(
    [result.riskratio, *result.riskratio_confint()],
    index=["point", "lcb", "ucb"],
    name="relative risk"
)
```

Return the odds ratio.

```python
pd.Series(
    [result.oddsratio, *result.oddsratio_confint()],
    index=["point", "lcb", "ucb"],
    name="odds ratio"
)
```

Return the result of a chi-square test for no association.

Note, `Table2x2` does have a method for this, but it returns a `Bunch`, a rather niche object that needs to be printed to the standard output.

```python
st.chi2_contingency(xtab, correction=False)
```

Return the result Fisher’s exact test.

```python
st.fisher_exact(xtab)
```
