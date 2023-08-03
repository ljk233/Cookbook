
# Datasets

## darwin

```toml
description="Paired data corresponding to the final height of corn data (Zea Mays)"
source="The Design of Experiments, 3rd edn, London, Oliver and Boyd, p. 27."
[schema]
    [schema.cross]
        description="Height of cross-fertilised parent"
        unit="inches"
        dtype="Real"
    [schema.self]
        description="Height of self-fertilised parent"
        unit="inches"
        dtype="Real"
```

## distance

```
description=Distances between twenty pairs of locations in Sheffield
source=Unattributed
schema:
    road    REAL    Distance by road (mi)
    map     REAL    Distance by map (straight-line) (mi)
```

## practicaltest

```
description=Percentage pass rates for 316 UK driving practical test centres (APR-2014 to MAR-2015)
source=UK Government
schema:
    centre  TEST    Test centre's name
    male    REAL    Male pass rate
    female  REAL    Female pass rate
    total   REAL    Total pass rate
```

## royaldeaths

```
description=Month of death of 82 descendants of Queen Victoria
source=Andrews, D. and Herzberg, A. (1985) Data, New York, Springer, p. 429
schema:
    month       INTEGER Month of death (January=1)
    n_deaths    INTEGER Number of deaths
```

## schoolgirls

```
description=Heights and weights of 30 eleven-year-old schoolgirls from Bradford. 
source=A.T. Graham, Open University
schema:
    height  INTEGER Height of participant (cm)
    weight  INTEGER Weight of participant (kg)
```

## skulls

```
description=Maximum head breadth of 84 Etruscan males and on 70 skulls of modern Italian males 
source=A.T. Graham, Open University
schema:
    skull   TEXT    Skull owner (Etruscan or Italian)
    breadth REAL    Maximum breath of skull (mm)
```

## tattoos

```toml
description="Clinical data from 55 patients who had forearm tattoos removed"
```
