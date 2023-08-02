# %% [markdown]
# # Fences
#
# ## Theory
#
# The upper and lower **fences** represent the cut-off values for upper
# and lower outliers.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(150, random_state=20230801), name="height")

# %% [markdown]
# Return the sample fences.

# %%
pd.Series(
    data={
        "lower": X.quantile(0.25) - 1.5 * st.iqr(X),
        "upper": X.quantile(0.75) + 1.5 * st.iqr(X),
    },
    name="fence",
)
