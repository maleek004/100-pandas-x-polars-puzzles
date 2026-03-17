# Puzzle 23. 
Given a DataFrame of numeric values, say
```python
df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values
```

how do you subtract the row mean from each element in the row?

```python
# ----  pandas solution
df = pd.DataFrame(np.random.random(size=(5, 3)))

row_means = df.mean(axis=1)

# 2. Subtract the means, aligning them with the rows (axis=0)
df.sub(row_means, axis=0)
```

```python
# ----  polars solution 

# to make the outut consistent we will make sure 
# the polars dataframe is a copy of the pandas one 

pldf = pl.from_pandas(df)

# Use horizontal mean across all columns
pldf.with_columns(pl.all() - pl.mean_horizontal(pl.all()))
```

