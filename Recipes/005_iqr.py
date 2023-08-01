# %% [markdown]
# # Sample interquartile-range
#
# ## Theory
#
# The **interquartile-range** (IQR) is difference between the first and the third quartiles.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Return the sample IQR.

# %%
st.iqr(X)
