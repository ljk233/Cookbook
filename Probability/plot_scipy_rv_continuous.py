"""Plot a SciPy continuous random variable."""

# %%
import numpy as np
import pandas as pd
from scipy import stats as st
from matplotlib import pyplot as plt
import seaborn as sns


# Initialise a binomial random variable
rv = st.norm()

# Plot the random variable
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), num=100)
pd.DataFrame(data={"X": x, "f": rv.pdf(x)}).pipe(sns.relplot, x="X", y="f", kind="line")
