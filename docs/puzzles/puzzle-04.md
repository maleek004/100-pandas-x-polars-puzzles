# Puzzle 4 - 21


## DataFrame basics

### A few of the fundamental routines for selecting, sorting, adding and aggregating data in DataFrames

Difficulty: *easy*

Before solving the puzzles below, remember to import NumPy (used here only for properly representing the missing values in the numeric column):
```python
import numpy as np
```
You will be working with the same underlying dataset for both Pandas and Polars puzzles.

Consider the following Python dictionary and list of row labels:


``` python
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```
(This is just some  made up data with the theme of animals and trips to a vet.)

## Puzzle 4 
Create a DataFrame `df` from the dictionary `data` above which has the index `labels`.

> Important note: Pandas has a first-class Index that is separate from the data columns. Polars does not maintain a persistent row index; if row labels are needed, they must be represented explicitly as a column.. This difference will matter in several puzzles below.

> ***A useful mental model is that Pandas behaves more like a spreadsheet—where rows have persistent labels, while Polars behaves more like a database or query engine, where data is primarily treated as a collection of columns and rows have no inherent identity unless explicitly added..*** - Gemini , last night

> Not having to manage a global index removes the need for row-level alignment and bookkeeping. This makes it easier for Polars to reorder, chunk, and parallelize operations, contributing to its performance.




```python
# ---- pandas solution


import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data,index=labels)

print(df)
```

```python
# ---- polars solution

pldf = (
    pl.DataFrame(data)
    .with_columns(pl.Series("index", labels)) # Add the index column
    .select(["index", pl.all().exclude("index")]) # Move 'index' to the left side for sanity's sake
)

print(pldf)
```

