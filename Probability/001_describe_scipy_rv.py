# %%
"""Return a description of a SciPy random variable.

Note, the standard deviation is rounded to 6dp.
There is no reason for this beyond comfort.
"""

from scipy import stats as st

# ======================================================================
# Get things ready
# ======================================================================

rv = st.binom(n=20, p=0.5)

# ======================================================================
# Return the random variable
# ======================================================================

desc_map = {"mean": rv.mean(), "std": rv.std().round(6)}
desc_map.update({f"q-{q}": rv.ppf(q) for q in [0.01, 0.25, 0.5, 0.75, 0.99]})
