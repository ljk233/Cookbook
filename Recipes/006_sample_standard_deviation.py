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
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample standard deviation.

# %%
X.std(ddof=1)
