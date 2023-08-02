# %% [markdown]
# # Count the number of missing values in a *pandas* `Series`
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Count of missing values.

# %%
X.isnull().sum()

# %% [markdown]
# Percentage missing values.

# %%
X.isnull().sum() / X.shape[0]

# %% [markdown]
# Summary: Number of rows, count of missing values, and percentage of missing values.

# %%
pd.Series(
    data={
        "nrows": X.shape[0],
        "count": X.isnull().sum(),
        "percent": X.isnull().sum() / X.shape[0],
    },
    name="missing values",
)
