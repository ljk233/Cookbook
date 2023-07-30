# %%
"""Return the approximate domain of a continuous random variable (rv_continuous)."""

import numpy as np
from scipy import stats as st


# ======================================================================
# Get things ready
# ======================================================================

rv = st.norm()

# ======================================================================
# Return the domain
# ======================================================================

np.linspace(rv.ppf(0.01), rv.ppf(0.99), num=50)
