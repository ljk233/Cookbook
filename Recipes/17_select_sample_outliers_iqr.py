# %% [markdown]
# # Select sample outliers using the IQR method
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
# Select the outliers.

# %%
lower_fence = X.quantile(0.25) - 1.5 * st.iqr(X)
upper_fence = X.quantile(0.75) + 1.5 * st.iqr(X)
X[X.between(lower_fence, upper_fence) == False]
