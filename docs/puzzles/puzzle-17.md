# Puzzle 17.
 Count the number of each type of animal in `df`.

```python
## ----  pandas solution
df['animal'].value_counts()
```

```python
# ----  Polars solution
pldf.group_by("animal").len()

# Alternative solution 
#   --   pldf['animal'].value_counts()
```

> [`.len()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.dataframe.group_by.GroupBy.len.html#polars.dataframe.group_by.GroupBy.len) (method): A group_by method that returns the number of rows in each group.

> [`.value_counts()`](https://docs.pola.rs/api/python/stable/reference/series/api/polars.Series.value_counts.html) (Method): A series method that Count the occurrences of unique values.

