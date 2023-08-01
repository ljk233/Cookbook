# %% [markdown]
# # Sample quintiles
#
# ## Theory
#
# The **sample quintiles** are the four values that separate a sample into five even parts.
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
X.quantile(np.linspace(0.2, 1, num=5)).rename("quintiles")
