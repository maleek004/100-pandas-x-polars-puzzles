# Puzzle  12.
 Select the rows where the age is between 2 and 4 (inclusive).

```python
# ---- pandas solution
df[df["age"].between(2, 4)]

# alternate pandas solution
#    df[(df.age >= 2) & (df.age <= 4)]
```

```python
# ---- polars solution

pldf.filter(pl.col("age").is_between(2, 4))

```

>  the [`is_between()`](https://docs.pola.rs/api/python/dev/reference/expressions/api/polars.Expr.is_between.html) method  can be used directly on a polars.Series or as part of an polars.Expr within operations like filter() or with_columns() to check if value(s) fall within a specified lower and upper bound

