"""Generate the domain of a SciPy discrete random variable."""

# %%
import numpy as np
from scipy import stats as st


# Initialise the random variable
rv = st.binom(n=20, p=0.5)

# Return the domain as a pandas Series
np.arange(rv.ppf(0.01), rv.ppf(0.99) + 1, dtype=int)
