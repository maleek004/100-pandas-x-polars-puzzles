# Puzzle 26 - 28

The next three puzzles are slightly harder.


## Puzzle26. 
In the cell below, you have a DataFrame `df` that consists of 10 columns of floating-point numbers. Exactly 5 entries in each row are NaN values. 

For each row of the DataFrame, find the *column* which contains the *third* NaN value.

You should return a Series of column labels: `e, c, d, h, d`

```python
nan = np.nan

data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],
        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],
        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],
        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],
        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]

columns = list('abcdefghij')

df = pd.DataFrame(data, columns=columns)

# ------ pandas solution


# 1. Create a boolean mask of NaNs
# 2. Cumulative sum across columns (axis=1). True counts as 1.
# 3. Find where the cumulative sum is exactly 3
# 4. idxmax along axis 1 returns the first column label where the condition is True
result = (df.isna().cumsum(axis=1) == 3).idxmax(axis=1)

print(result.tolist())
```

```python
# ------ polars solution

pldf = pl.from_pandas(df)
# 1. Map column names to their index
column_names = pldf.columns

# 2. Use a horizontal expression to find column indices where values are null
# 3. Extract the 3rd index (index 2) from that list
result = pldf.select(
    pl.struct(pl.all())
    .map_elements(lambda row: [k for k, v in row.items() if v is None][2], return_dtype=pl.String)
).to_series()

print(result.to_list())
```

