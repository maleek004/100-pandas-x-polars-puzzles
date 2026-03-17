# Puzzle  15.
 Calculate the mean age for each different animal in `df`.

```python
# ----  pandas solution
df.groupby('animal')['age'].mean()
```

```python
# ---- polars solution
print(pldf.group_by("animal", maintain_order=True).agg(pl.col("age").mean()))
```

> The [`.group_by()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.group_by.html) (Context): Segregates the data into "buckets" based on unique values in a column. after which you can then apply aggregation functions using [`.agg()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.dataframe.group_by.GroupBy.agg.html#polars.dataframe.group_by.GroupBy.agg)

> The maintain_order=True parameter ensures that the group order is retained, but makes the process a little slower 

