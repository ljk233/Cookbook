"""Plot a SciPy discrete random variable as a bar plot."""

# %%
import numpy as np
import pandas as pd
from scipy import stats as st
from matplotlib import pyplot as plt
import seaborn as sns


# Initialise a binomial random variable
rv = st.binom(n=20, p=0.5)

# Plot the random variable
x = np.arange(rv.ppf(0.01), rv.ppf(0.99) + 1, dtype=int)
pd.DataFrame(data={"X": x, "p": rv.pmf(x)}).pipe(
    sns.catplot, x="X", y="p", kind="bar", color="cornflowerblue"
)