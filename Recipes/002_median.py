# %% [markdown]
# # Median
#
# ## Theory
#
# The **median** is the value that minimises the sum of absolute deviations.
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
# Return the sample median.

# %%
X.median()
