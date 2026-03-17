# Puzzle 31. 
You are given the DataFrame below with a column of group IDs, 'grps', and a column of corresponding integer values, 'vals'.

```python
df = pd.DataFrame({"vals": np.random.RandomState(31).randint(-30, 30, size=15), 
                   "grps": np.random.RandomState(31).choice(["A", "B"], 15)})
```

Create a new column 'patched_values' which contains the same values as the 'vals' any negative values in 'vals' with the group mean:

```
    vals grps  patched_vals
0    -12    A          13.6
1     -7    B          28.0
2    -14    A          13.6
3      4    A           4.0
4     -7    A          13.6
5     28    B          28.0
6     -2    A          13.6
7     -1    A          13.6
8      8    A           8.0
9     -2    B          28.0
10    28    A          28.0
11    12    A          12.0
12    16    A          16.0
13   -24    A          13.6
14   -12    A          13.6
```

```python
# ---- pandas solution

df = pd.DataFrame({"vals": np.random.RandomState(31).randint(-30, 30, size=15), 
                   "grps": np.random.RandomState(31).choice(["A", "B"], 15)})

# 1. Calculate the mean of POSITIVE values only for each group
# We mask negative values to NaN so they don't influence the mean
def mean_positive(x):
    return x[x > 0].mean()

group_means = df.groupby('grps')['vals'].transform(mean_positive)

# 2. Use np.where to choose between the original value and the group mean
df['patched_vals'] = np.where(df['vals'] < 0, group_means, df['vals'])

df
```

```python
# ------ polars solution

pldf = pl.from_pandas(df)

# 1. Calculate the mean of values > 0 per group using a window expression
# 2. Use when/then logic to apply the patch
result = pldf.with_columns(
    patched_vals = pl.when(pl.col("vals") < 0)
    .then(
        pl.col("vals").filter(pl.col("vals") > 0).mean().over("grps")
    )
    .otherwise(pl.col("vals"))
)

result
```

