"""Summarising a single categorical variable."""

# %%
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

# %% Cache the data
smoke_ban = sm.datasets.get_rdataset("SmokeBan", "AER", cache=True)
smoker_se: pd.Series = smoke_ban.data["smoker"]

# %%  Counts
smoker_se.value_counts()

# %%  Proportions
smoker_se.value_counts(normalize=True)

# %% Percentages
smoker_se.value_counts(normalize=True) * 100

# %% Visuable the aggregation
sns.countplot(x=smoker_se)
