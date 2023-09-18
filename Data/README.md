
# Data catalogue

## `cholesterol`

```toml
summary = "Plasma levels of total cholesterol in 24 adults with hyperlipoproteinaemia"
source = "Krzanowski, W.J. (1998) An Introduction to Statistical Modelling, London, Arnold, Chapter 3"
file_path = "./data/darwin.csv"
[schema]
    [schema.cholesterol]
    description = "Total cholesterol level"
    unit = "mg/ml"
    data_type = "Real"
    [schema.age]
    description = "Age"
    unit = "Years"
    data_type = "Integer"
```

## `coin`

```toml
summary = """Silver content of twelfth-century Byzantine coins minted during different
periods of the reign of Manuel I Comnenus
"""
source = """Hendy, M.F. and Charles, J.A. (1970) ‘The production techniques, silver
content and circulation history of the twelfth-century Byzantine trachy’,
Archaeometry, vol. 12, no. 1, pp. 13–21)
"""
file_path = "./Data/coin.parquet"
[schema]
    [schema.coinage]
    description = "Coinage of coin (A, B, C, D)"
    unit = "Null"
    data_type = "Text"
    [schema.pct_Hg]
    description = "Silver content"
    unit = "Percent"
    data_type = "Real"
```

## `darwin`

```toml
summary = "Paired data corresponding to the final height of corn data (Zea Mays)"
source = "The Design of Experiments, 3rd edn, London, Oliver and Boyd, p. 27."
file_path = "./data/darwin.csv"
[schema]
    [schema.cross]
    description = "Height of cross-fertilised parent"
    unit = "Inch"
    data_type = "Real"
    [schema.self]
    description = "Height of self-fertilised parent"
    unit = "Inch"
    data_type = "Real"
```

## `practicaltest`

```toml
summary = "Percentage pass rates for 316 UK driving practical test centres (APR-2014 to MAR-2015)"
source = "UK Government"
file_path = "./data/practicaltest.csv"
[schema]
    [schema.centre]
    description = "Test centre's name"
    unit = "Null"
    data_type = "Text"
    [schema.male]
    description = "Male pass rate"
    unit = "Null"
    data_type = "Real"
    [schema.female]
    description = "Female pass rate"
    unit = "Null"
    data_type = "Real"
    [schema.total]
    description = "Total pass rate"
    unit = "Null"
    data_type = "Real"
```

## `royaldeath`

```toml
summary = "Month of death of 82 descendants of Queen Victoria"
source = "Andrews, D. and Herzberg, A. (1985) Data, New York, Springer, p. 429"
file_path = "./data/royaldeath.csv"
[schema]
    [schema.month]
    description = "Month of death (1=January, 12=December)"
    unit = "Null"
    data_type = "Integer"
    [schema.n_deaths]
    description = "Number of deaths"
    unit = "Null"
    data_type = "Integer"
```

## `schoolgirl`

```toml
summary = "Heights and weights of 30 eleven-year-old schoolgirls from Bradford, UK."
source = "A.T. Graham, Open University"
file_path = "./data/schoolgirl.csv"
[schema]
    [schema.height]
    description = "Participant's height"
    unit = "Centimetre"
    data_type = "Integer"
    [schema.weight]
    description = "Participant's weight"
    unit = "Kilogram"
    data_type = "Integer"
```

## `skull`

```toml
summary = "Maximum head breadth of 84 Etruscan males and on 70 skulls of modern Italian males."
source = """Barnicot, N.A. and Brothwell, D.R. (1959) ‘The evaluation of metrical
data in the comparison of ancient and modern bones’, in Wolstenholme, G.E.W. and
O’Connor, C.M. (eds) Medical Biology and Etruscan Origins, Boston, Little, Brown & Co.
"""
file_path = "./data/skull.csv"
[schema]
    [schema.skull]
    description = "Skull owner ('Etruscan', 'Italian')"
    unit = "Null"
    data_type = "Text"
    [schema.breadth]
    description = "Maximum breath of skull"
    unit = "Millimetre"
    data_type = "Real"
```

## `survey`

```toml
summary = "Responses of 237 Statistics I students at the University of Adelaide to a number of questions."
source = """Venables, W. N. and Ripley, B. D. (2002) Modern Applied Statistics with S-PLUS.
Fourth Edition. Springer.
"""
file_path = "./data/survey.ddb"
[schema]
    [schema.sex]
    description = "Sex of student (Male, Female)"
    unit = "Null"
    data_type = "Text"
    [schema.writing_hand_span]
    description = "Span of student's writing hand"
    unit = "Centimetre"
    data_type = "Real"
    [schema.non_writing_hand_span]
    description = "Span of student's non-writing hand"
    unit = "Centimetre"
    data_type = "Real" 
    [schema.arm_fold]
    description = "Fold your arms! Which is on top? (R on L, L on R, Neither)"
    unit = "Null"
    data_type = "Text"
    [schema.pulse]
    description = "Pulse rate"
    unit = "Beats per minute"
    data_type = "Integer"
    [schema.clap_hand]
    description = "Clap your hands! Which hand is on top? (Left, Right, Neither)"
    unit = "Null"
    data_type = "Text"
    [schema.exercise_frequency]
    description = "How often the student exercises (None, Some, Freq)"
    unit = "Null"
    data_type = "Text"
    [schema.smoke_frequency]
    description = "How much the student smokes (Never, Occas, Regul, Heavy)"
    unit = "Null"
    data_type = "Text"
    [schema.height]
    description = "Height of the student"
    unit = "Centimetre"
    data_type = "REAL"
    [schema.measurement]
    description = "Whether the student expressed height in imperial or metric units (Imperial, Metric)"
    unit = "Null"
    data_type = "Text"
    [schema.age]
    description = "Age of the student"
    unit = "Years"
    data_type = "Real"
```

## `tattoo`

```toml
summary = "Clinical data from 55 patients who had forearm tattoos removed."
source = "Lunn, A.D. and McNeil, D.R. (1988) The SPIDA Manual, Statistical Computing Laboratory, Sydney"
file_path = "./data/tattoo.csv"
[schema]
    [schema.method]
    description = "Removal method (A, B)"
    unit = "Null"
    data_type = "Text"
    [schema.gender]
    description = "Participant's gender (m, f)"
    unit = "Null"
    data_type = "Text"
    [schema.size]
    description = "Tattoo size (large, med, small)"
    unit = "Null"
    data_type = "Text"
    [schema.depth]
    description = "Tattoo's depth (deep, mod)"
    unit = "Null"
    data_type = "Text"
    [schema.score]
    description = "Success rating (Likert scale) (1=poor, 4=excellent)"
    unit = "Null"
    data_type = "Integer"
```
