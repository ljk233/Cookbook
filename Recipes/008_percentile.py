# %% [markdown]
# # *N*th percentile
#
# ## Theory
#
# The ***n*th percentile** is the value *p* such that *n*% of the
# observations are lower and (100 - *n*)% of the observations are
# greater than *p*.
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
# Return *q*-0.05.

# %%
X.quantile(0.05)
