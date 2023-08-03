
# Datasets

## darwin

```toml
# darwin = pd.read_csv("../data/darwin.csv")
summary = "Paired data corresponding to the final height of corn data (Zea Mays)"
source = "The Design of Experiments, 3rd edn, London, Oliver and Boyd, p. 27."
file_path = "./data/darwin.csv"
[schema]
    [schema.cross]
    description = "Height of cross-fertilised parent"
    unit = "Inch"
    dtype = "Real"
    [schema.self]
    description = "Height of self-fertilised parent"
    unit = "Inch"
    dtype = "Real"
```

## distance

```toml
# distance = pd.read_csv("../data/distance.csv")
summary = "Distances between pairs of locations in Sheffield"
source = "Unattributed"
file_path = "./data/distance.csv"
[schema]
    [schema.road]
    description = "Distance by road"
    unit = "Mile"
    dtype = "Real"
    [schema.map]
    description = "Straight-line distance by map"
    unit = "Mile"
    dtype = "Real"
```

## practicaltest

```toml
# practicaltest = pd.read_csv("../data/practicaltest.csv")
summary = """Percentage pass rates for 316 UK driving practical test centres,
APR-2014 to MAR-2015
"""
source = "UK Government"
file_path = "./data/practicaltest.csv"
[schema]
    [schema.centre]
    description = "Test centre's name"
    unit = "Null"
    dtype = "Text"
    [schema.male]
    description = "Male pass rate"
    unit = "Null"
    dtype = "Real"
    [schema.female]
    description = "Female pass rate"
    unit = "Null"
    dtype = "Real"
    [schema.total]
    description = "Total pass rate"
    unit = "Null"
    dtype = "Real"
```

## royaldeath

```toml
# royaldeath = pd.read_csv("../data/royaldeath.csv")
summary = "Month of death of 82 descendants of Queen Victoria"
source = "Andrews, D. and Herzberg, A. (1985) Data, New York, Springer, p. 429"
file_path = "./data/royaldeath.csv"
[schema]
    [schema.month]
    description = "Month of death (1=January, 12=December)"
    unit = "Null"
    dtype = "Integer"
    [schema.n_deaths]
    description = "Number of deaths"
    unit = "Null"
    dtype = "Integer"
```

## schoolgirl

```toml
# schoolgirl = pd.read_csv("../data/schoolgirl.csv")
summary = "Heights and weights of 30 eleven-year-old schoolgirls from Bradford."
source = "A.T. Graham, Open University"
file_path = "./data/schoolgirl.csv"
[schema]
    [schema.height]
    description = "Participant's height"
    unit = "Centimetre"
    dtype = "Integer"
    [schema.weight]
    description = "Participant's weight"
    unit = "Kilogram"
    dtype = "Integer"
```

## skull

```toml
# skull = pd.read_csv("../data/skull.csv"")
summary = """Maximum head breadth of 84 Etruscan males and on 70 skulls of modern
Italian males 
"""
source = """Barnicot, N.A. and Brothwell, D.R. (1959) ‘The evaluation of metrical
data in the comparison of ancient and modern bones’, in Wolstenholme, G.E.W. and
O’Connor, C.M. (eds) Medical Biology and Etruscan Origins, Boston, Little, Brown & Co.
"""
file_path = "./data/skull.csv"
[schema]
    [schema.skull]
    description = "Skull owner ('Etruscan', 'Italian')"
    unit = "Null"
    dtype = "Text"
    [schema.breadth]
    description = "Maximum breath of skull"
    unit = "Millimetre"
    dtype = "Real"
```

## tattoo

```toml
# tattoo = pd.read_csv("../data/tattoo.csv")
summary = "Clinical data from 55 patients who had forearm tattoos removed"
source = """Lunn, A.D. and McNeil, D.R. (1988) The SPIDA Manual, Statistical
Computing Laboratory, Sydney
"""
file_path = "./data/tattoo.csv"
[schema]
    [schema.method]
    description = "Removal method ('A', 'B')"
    unit = "Null"
    dtype = "Text"
    [schema.gender]
    description = "Participant's gender ('m', 'f')"
    unit = "Null"
    dtype = "Text"
    [schema.size]
    description = "Tattoo size ('large', 'med', 'small')"
    unit = "Null"
    dtype = "Text"
    [schema.depth]
    description = "Tattoo's depth ('deep', 'mod')"
    unit = "Null"
    dtype = "Text"
    [schema.score]
    description = "Success rating (Likert scale) (1=poor, 4=excellent)"
    unit = "Null"
    dtype = "Integer"
```
