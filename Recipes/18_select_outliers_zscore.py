# %% [markdown]
# # Select sample outliers using the *z*-score method
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(st.norm(170, 10).rvs(1_000, random_state=21), name="height")

# %% [markdown]
# Select the outliers.

# %%
X[st.zscore(X).between(-3, 3) == False]
