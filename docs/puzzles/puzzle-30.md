# Puzzle 30. 
Consider the DataFrame constructed below which contains rows and columns of numerical data. 

Create a list of the column-row index locations of the 3 largest values in this DataFrame. In this case, the answer should be:
```
[(5, 7), (6, 4), (2, 5)]
```

```python
# ---- pandas solution

df = pd.DataFrame(np.random.RandomState(30).randint(1, 101, size=(8, 8)))

# 1. Unstack the dataframe into a Series (this creates a MultiIndex of [col, row])
# 2. Sort by values descending
# 3. Take the top 3 and extract the index (the coordinates)
df.unstack().sort_values(ascending=False).head(3).index.tolist()
```

```python
# ------ polars  solution
pldf = pl.from_pandas(df)

# 1. Add a row index so we can track coordinates
# 2. Melt to long format (columns: row_idx, variable (column_name), value)
# 3. Sort by value and take top 3
# 4. Extract (column, row) pairs
top_3 = (
    pldf.with_row_index("row_idx")
    .unpivot(index="row_idx")
    .sort("value", descending=True)
    .head(3)
)

# Convert to the specific list of tuples format (column_int, row_int)
result = [
    (int(col), row) 
    for col, row in zip(top_3["variable"], top_3["row_idx"])
]

print(result)

```

