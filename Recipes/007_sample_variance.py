# %% [markdown]
# # Sample variance
#
# ## Theory
#
# The **sample standard deviation** is the average squared difference of the scores from the mean.
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
# Return the sample variance.

# %%
X.var(ddof=1)
