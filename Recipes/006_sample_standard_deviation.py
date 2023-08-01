# %% [markdown]
# # Sample standard deviation
#
# ## Theory
#
# The **sample standard deviation** is the positive square root of the *sample variance*.
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
# Return the sample standard deviation.

# %%
X.std(ddof=1)
