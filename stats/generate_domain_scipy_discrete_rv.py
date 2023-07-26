"""Generate the domain of a SciPy discrete random variable."""

# %%
import numpy as np
from scipy.stats import binom


def domain(rv):
    return np.arange(rv.ppf(0.01), rv.ppf(0.99))


# Example
# =======
x = binom(20, 0.5)
print(domain(x))

# [ 5.  6.  7.  8.  9. 10. 11. 12. 13. 14.]
