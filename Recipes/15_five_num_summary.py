# %% [markdown]
# # Five-number summary
#
# ## Theory
#
# [The] five-number summary simply consists of the smallest data value,
# the first quartile, the median, the third quartile, and the largest data
# value.
# A *box plot* is a graphical device based on a five-number summary.
#
# ## Aside
#
# We don't recommend this recipe is used, because all of the values in the
# *five-number summary* are included in the `describe()` method of a `DataFrame`.
#
# It is included for user who like to be explicit when performing their data anlysis.
#
# ## Recipe
#
# Load the dependencies.

# %%
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
from matplotlib import pyplot as plt

# %% [markdown]
# Get things ready.

# %%
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# %% [markdown]
# Return the five-number summary.

# %%
pd.Series(
    data={
        "min": X.min(),
        "lower quartile": X.quantile(0.25),
        "median": X.median(),
        "upper quartile": X.quantile(0.75),
        "max": X.max(),
    },
    name="five-number summary",
)
