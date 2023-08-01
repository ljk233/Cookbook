# %% [markdown]
# # Q-Q plot
#
# ## Theory
#
# The **Q-Q plot**, or *quantile to quantile* plot, is a graph that tests the
# conformity between the empirical distribution and the given theoretical
# distribution.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
from matplotlib import pyplot as plt

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Plot the Q-Q plot.

# %%
res = st.probplot(X, plot=plt)
