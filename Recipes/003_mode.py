# %% [markdown]
# # Mode
#
# ## Theory
#
# The **mode** is the value of the observation that has the highest frequency.
#
# ## Recipe
#
# Load the dependencies.

# %%
from random import choices
import pandas as pd

# %% [markdown]
# Get things ready.

# %%
X = pd.Series(choices(["fail", "pass", "merit", "distinction"], k=40), name="grade")

# %% [markdown]
# Return the sample mode.

# %%
X.value_counts().head(1)
