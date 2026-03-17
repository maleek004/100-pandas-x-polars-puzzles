# Puzzle  7.
 Select just the 'animal' and 'age' columns from the DataFrame `df`.

```python
# ----  Pandas solution

df[['animal','age']]
```

```python
# ----  Polars solution

pldf.select(["animal", "age"])
```

> this is one of the key difference in how pandas works vs polars : how dataframe is sliced

> loc[] and iloc[] are not available in polars ( again : because no index). Because of this you need to rely on expressions like [`.select()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.select.html#polars.DataFrame.select) and .[`filter()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.filter.html#polars.DataFrame.filter)

