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
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample quartiles.

# %%
X.quantile(np.linspace(0.25, 1, num=4)).rename("quartiles")
