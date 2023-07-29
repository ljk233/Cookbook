"""Summarising a single categorical variable."""

# %% Import dependencies
import pandas as pd
import seaborn as sns
import statsmodels.api as sm


sns.set_theme()

# %% Cache the data
X: pd.DataFrame = sm.datasets.get_rdataset("SmokeBan", "AER", cache=True).data

# ======================================================================
# Numeric summaries
# ======================================================================

# %% Counts
X["smoker"].value_counts()

# %% Proportions
X["smoker"].value_counts(normalize=True)

# %% Percentages
X["smoker"].value_counts(normalize=True).mul(100).rename("percentage")

# ======================================================================
# Visualisations
# ======================================================================

# %% Simple bar plot (y=count)
sns.countplot(x=X)

# %% Simple bar plot (y=proportion)
X[["smoker"]].value_counts(normalize=True).reset_index().pipe(
    sns.catplot, x="smoker", y="proportion", kind="bar"
)
