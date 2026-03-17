# Puzzle 10.
 Select the rows where the age is missing, i.e. it is `NaN`.

```python
# ----  pandas solution
df[df.age.isnull()] # PS: isna() is an alias for isnull()
```

```python
# ----  polars solution
pldf.filter(pl.col("age").is_null())
```

