# %% [markdown]
# # Range
#
# ## Theory
#
# The **Range** is the difference between the highest observed value and the lowest observed value.
#
# ## Recipe
#
# Load the dependencies.

# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Return the sample range.

np.ptp(X)
