# %%
"""Return the approximate domain of a continuous random variable (rv_continuous)."""

import numpy as np
from scipy import stats as st


# ======================================================================
# Get things ready
# ======================================================================

rv = st.binom(10, 0.7)

# ======================================================================
# Return the domain
# ======================================================================

np.arange(rv.ppf(0.01), rv.ppf(0.99) + 1, dtype=int)
