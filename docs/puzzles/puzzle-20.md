# Puzzle 20 
In the 'animal' column, change the 'snake' entries to 'python'.

```python
# ----  Pandas solution

df["animal"] = df['animal'].replace("snake", "python")
df
```

Knowing when to use map() or replace() in pandas : 
>You cannot use map to change values in a column when you don't know all the possible values that already exist in the column. If you do so , any value that you miss in your map will be replaced with Nan. For cases like this , you can just use replace() to change only the values that you know

```python
# ----  polars solution
pldf = pldf.with_columns(pl.col("animal").replace("snake", "python"))
pldf
```

> [`replace()`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.replace.html#polars.Expr.replace) : an expression method, replaces a single value by another value. Values that were not replaced remain unchanged.

