# Puzzle  14.
Calculate the sum of all visits in `df` (i.e. find the total number of visits).

```python
# ----  pandas solution
df["visits"].sum()
```

```python
# ----  polars solution
pldf.select(pl.col("visits").sum()).item()
```

> The polars dataframe's [`.item()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.item.html) method can be used to return the element at a given cell  or a 1x1 dataframe (which is the case above) as a scalar value

