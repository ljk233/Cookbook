"""Summarising a single numarical variable."""

# %% Import dependencies
import pandas as pd
import statsmodels.api as sm
import seaborn as sns


sns.set_theme()

# %% Cache the data and transform
X: pd.DataFrame = sm.datasets.get_rdataset("Davis", "carData", cache=True).data.dropna()

# ======================================================================
# Numeric summaries
# ======================================================================

# %% Mean, standard deviation, and five-number summary
X["height"].describe()

# %% Range
X["height"].max() - X["height"].min()

# %% Interquartile range
X["height"].quantile(0.75) - X["height"].quantile(0.25)

# %% Sample standard deviation (Aso works with var() method)
X["height"].std(ddof=1)

# ======================================================================
# Visualisations
# ======================================================================

# %% Proability histrogram
sns.displot(data=X, x="height", kind="hist", stat="probability")

# %% Box-plot
sns.catplot(data=X, x="height", kind="box")
