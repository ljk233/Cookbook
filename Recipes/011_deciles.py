# %% [markdown]
# # Deciles
#
# ## Theory
#
# The **deciles** are the nine values that separate a sample into 10 even parts.
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
# Return the sample quartiles.

# %%
X.quantile(np.linspace(0.1, 1, num=10)).rename("deciles")
