"""Return a description of a SciPy random variable."""

# %%
import pandas as pd
from scipy import stats as st

# Initialise the random variable
rv = st.binom(n=20, p=0.5)

# Collect the description
desc_map = {"mean": rv.mean(), "std": rv.std()}
desc_map.update({f"q-{q}": rv.ppf(q) for q in [0.01, 0.25, 0.5, 0.75, 0.99]})

# Return the description as a pandas Series
pd.Series(desc_map, name="description")
