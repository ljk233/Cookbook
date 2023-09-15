
# Mann-Whitney *U* test

*2023-09-15*

The **Mann-Whitney *U* test:**

- is used to compare two independent samples
- is a nonparametric alternative to the two sample *t*-test for independent samples
- does not assumed the data are normally distributed
- has a test statistic *U*, which is the sum of the ranks for one of the samples
- is also known as the *Wilcoxon rank sum test*

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
coin = pd.read_parquet("../data/coin.parquet")
```

The hypotheses are,

&ensp;&ensp;&ensp;&ensp;
H<sub>0</sub> : *m*<sub>A</sub> = *m*<sub>D</sub>;
H<sub>1</sub> : *m*<sub>A</sub> ≠ *m*<sub>D</sub>,

where *m*<sub>A</sub>, *m*<sub>D</sub> are the median percentage silver content of a coin in samples A and D, respectively.

Select the coins from samples A and D.

```python
A = coin.query("coinage == 'A'")["pct_Hg"]
D = coin.query("coinage == 'D'")["pct_Hg"]
```

Return the result of the hypothesis test.

```python
st.mannwhitneyu(A, D)
```

## References

- *Non-parametric and goodness-of-fit tests* (M248, 2019)
- *[Mann Whitney U Test](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_nonparametric/BS704_Nonparametric4.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
