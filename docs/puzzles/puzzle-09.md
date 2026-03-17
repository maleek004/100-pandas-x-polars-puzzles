# Puzzle 9.
 Select only the rows where the number of visits is greater than 3.

```python
# ----  pandas  SOlution
df[df.visits > 3]
```

```python
# ----  polars  Solution
pldf.filter(pl.col("visits") > 3)
```

> For this puzzle we have introduced these in polars: 
> - .filter() method 
> - and the [`pl.col()`](https://docs.pola.rs/api/python/stable/reference/expressions/col.html) constructor 

