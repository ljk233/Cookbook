# %% [markdown]
# # Sample mode
#
# ## Theory
#
# The **sample mode** is the value of the observation that has the highest frequency.
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
X: pd.Series = sm.datasets.get_rdataset("SwissLabor", "AER").data["oldkids"]

# %% [markdown]
# Return the sample mode.

# %%
X.value_counts().head(1)
