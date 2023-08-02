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
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample variance.

# %%
X.var(ddof=1)
