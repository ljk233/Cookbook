# %% [markdown]
# # Mean
#
# ## Theory
#
# The **mean** is the value that minimises the sum of the squared deviations.
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
# Return the sample mean.

# %%
X.mean()
