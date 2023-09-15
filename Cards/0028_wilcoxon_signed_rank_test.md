
# Wilcoxon signed rank test

*2023-09-15*

## Notes

The **Wilcoxon signed rank test:**

- is used to compare two matched samples, or to conduct a paired difference test of repeated measurements on a single sample to assess whether their population mean ranks differ
- is a nonparametric alternative to the matched *t*-test for dependent samples
- does not assume the sample is normally distributed
- has a test value *W*, which is the smaller number of plus or minus signs
  - If the sample size *n* ≥ 25, then a normal approximation can be used to find the test value

Note, any differences of 0 should be discarded.

## Example

Import the dependencies.

```python
import pandas as pd
from scipy import stats as st
```

Load the data.

```python
darwin = pd.read_parquet("../data/darwin.parquet")
```

The hypotheses are,

&ensp;&ensp;&ensp;&ensp;
H<sub>0</sub> : μ<sub>D</sub> = 0;
H<sub>1</sub> : μ<sub>D</sub> ≠ 0,

where *D* = *X* - *S* is the median difference between the heights of paired cross- and self-fertilised plants.

Return the result of the hypothesis test.

```python
st.wilcoxon(darwin["cross"], darwin["self"])
```

Alternatively, we could take the difference ourselves to return the same result.

```python
st.wilcoxon(darwin["cross"] - darwin["self"])
```

## References

- *Non-parametric and goodness-of-fit tests* (M248, 2019)
- *[Wilcoxon Signed Rank Test](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_nonparametric/BS704_Nonparametric6.html#headingtaglink_1)* (Boston University School of Public Health, 2017)
