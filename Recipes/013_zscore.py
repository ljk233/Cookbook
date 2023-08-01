# %% [markdown]
# # Sample *z*-scores
#
# ## Theory
#
# The ***z*-score** is the number of standard deviations a value is away
# from the *sample mean*.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Return the sample *z*-scores.

# %%
pd.Series(st.zscore(X), name="zscore")
