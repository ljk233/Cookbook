"""Return the five-number summary of some data by calling the describe method."""

# %%
import pandas as pd
from scipy.stats import binom


# Examples
# ========
df = pd.DataFrame({"x": binom(20, 0.6).rvs(50), "y": binom(20, 0.45).rvs(50)})

# One variable
# ============
df.describe()

# Multiple variables
# ==================
df.melt().groupby("variable").describe()
