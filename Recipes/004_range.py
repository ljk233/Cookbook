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
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample range.

np.ptp(X)
