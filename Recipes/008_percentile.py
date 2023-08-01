# %% [markdown]
# # *N*th percentile
#
# ## Theory
#
# The ***n*th percentile** is the value *p* such that *n*% of the
# observations are lower and (100 - *n*)% of the observations are
# greater than *p*.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
import statsmodels.api as sm

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Return *q*-0.05.

# %%
X.quantile(0.05)
