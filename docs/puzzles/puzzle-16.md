# Puzzle 16. 
Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

```python
# ----  pandas  solution
df.loc['k'] = ['dog', 5.5, 2, 'no']
print(df)
df.drop('k', inplace=True)
```

```python
# ----  Polars solution
new_row = pl.DataFrame({"index": ["k"], "animal": ["dog"], "age": [5.5], "visits": [2], "priority": ["no"]})
# add the row
pldf = pl.concat([pldf, new_row])
pldf

# delete the row 
pldf = pldf.filter(pl.col("index") != "k")
```

> [`pl.concat()`](https://docs.pola.rs/api/python/stable/reference/api/polars.concat.html#polars.concat) (Function): Stitches two separate DataFrames or LazyFrames together vertically or horizontally.

> The mental logic for "dropping" inpolars is to run a "select" that leaves out the rows you intend to drop

