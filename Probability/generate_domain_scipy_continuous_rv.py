"""Generate the domain of a SciPy continuous random variable."""

# %%
import numpy as np
import pandas as pd
from scipy import stats as st


# Initialise the random variable
rv = st.norm()

# Return the domain as a np.array
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), num=50)

# Return the domain as a pd.Series
x_se = pd.Series(x, name="X")
