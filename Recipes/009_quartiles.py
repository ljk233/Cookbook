# %% [markdown]
# # Quartiles
#
# ## Theory
#
# The **quartiles** are the three values that separate a sample into four even parts.
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
X.quantile(np.linspace(0.25, 1, num=4)).rename("quartiles")
