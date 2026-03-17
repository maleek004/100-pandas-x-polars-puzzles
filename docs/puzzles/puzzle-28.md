# Puzzle 28. 
The DataFrame `df` constructed below has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive). 

For each group of 10 consecutive integers in 'A' (i.e. `(0, 10]`, `(10, 20]`, ...), calculate the sum of the corresponding values in column 'B'.

The answer should be a Series as follows:

```
A
(0, 10]      635
(10, 20]     360
(20, 30]     315
(30, 40]     306
(40, 50]     750
(50, 60]     284
(60, 70]     424
(70, 80]     526
(80, 90]     835
(90, 100]    852
```

```python
df = pd.DataFrame(np.random.RandomState(8765).randint(1, 101, size=(100, 2)), columns = ["A", "B"])

# ------ pandas solution

# 1. Define the bin edges (0, 10, 20, ..., 100)
bins = np.arange(0, 101, 10)

# 2. Use pd.cut to assign each 'A' value to a bin
# 3. Group by these bins and sum 'B'
result = df.groupby(pd.cut(df['A'], bins))['B'].sum()

print(result)
```

```python
# ---- polars solution

pldf = pl.from_pandas(df)

# 1. Create a grouping column using math: ((A-1) // 10) gives 0 for 1-10, 1 for 11-20, etc.
# 2. Map those integers back to the string labels for the final output
result = (
    pldf.with_columns(
        group_id=((pl.col("A") - 1) // 10)
    )
    .group_by("group_id")
    .agg(pl.col("B").sum())
    .sort("group_id")
    .with_columns(
        A=(pl.col("group_id") * 10).cast(pl.String) + "-" + (pl.col("group_id") * 10 + 10).cast(pl.String)
    )
    .select(["A", "B"])
)

print(result)
```

