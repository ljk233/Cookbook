# %% [markdown]
# # Sample *z*-scores
#
# ## Theory
#
# The ***z*-score** is the number of standard deviations a value is away
# from the *sample mean*.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample *z*-scores.

# %%
pd.Series(st.zscore(X), name="zscore")
