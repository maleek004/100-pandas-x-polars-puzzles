# Puzzle 29 - 32

## DataFrames: harder problems 

### These might require a bit of thinking outside the box...

...but all are solvable using just the usual pandas/NumPy methods (and so avoid using explicit `for` loops).

Difficulty: *hard*

## Puzzle 29 
Consider a DataFrame `df` where there is an integer column 'X':
```python
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
```
For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer). These values should therefore be 

```
[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]
```

Make this a new column 'Y'.

```python
# ---- pandas solution

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# 1. Identify where X is 0
izero = (df['X'] == 0)

# 2. Create a 'group' ID that increments every time a 0 appears
# This gives us: [0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
abs_zeros = izero.cumsum()

# 3. Use cumulative count within these groups.
# We then add 1 to the count, but reset it to 0 specifically where the original value was 0.
df['Y'] = df.groupby(abs_zeros).cumcount()

# The first group (before any zero) needs an offset because there was no zero to 'start' it
# We find the index of the first zero to determine how to adjust the first group
first_zero_idx = (df['X'] == 0).idxmax()
df.loc[:first_zero_idx-1, 'Y'] += 1
df.loc[df['X'] == 0, 'Y'] = 0

print(df['Y'].tolist())
```

```python
# ------ polars solution

pldf = pl.from_pandas(df)

# 1. Create a boolean column for zeros
# 2. Use cum_sum on the booleans to create "windows" or "groups"
# 3. Inside those windows, count the rows
result = pldf.with_columns(
    group=pl.col("X").eq(0).cum_sum()
).with_columns(
    Y=pl.int_range(0, pl.len()).over("group")
)

# Adjusting for the 'pre-zero' values (they should count from the start)
# and ensuring zeros stay zero.
first_zero_index = pldf.select(pl.arg_where(pl.col("X") == 0)).item(0, 0)

result = result.with_columns(
    Y = pl.when(pl.col("X") == 0)
        .then(0)
        .when(pl.col("group") == 0)
        .then(pl.col("Y") + 1)
        .otherwise(pl.col("Y"))
).select("X", "Y")

print(result["Y"].to_list())
```

