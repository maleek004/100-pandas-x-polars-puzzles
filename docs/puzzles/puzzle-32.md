# Puzzle 32. 
Implement a rolling mean over groups with window size 3, which ignores NaN value. For example consider the following DataFrame:

```python
>>> df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})
>>> df
   group  value
0      a    1.0
1      a    2.0
2      b    3.0
3      b    NaN
4      a    2.0
5      b    3.0
6      b    NaN
7      b    1.0
8      a    7.0
9      b    3.0
10     a    NaN
11     b    8.0
```
The goal is to compute the Series:

```
0     1.000000
1     1.500000
2     3.000000
3     3.000000
4     1.666667
5     3.000000
6     3.000000
7     2.000000
8     3.666667
9     2.000000
10    4.500000
11    4.000000
```
E.g. the first window of size three for group 'b' has values 3.0, NaN and 3.0 and occurs at row index 5. Instead of being NaN the value in the new column at this row index should be 3.0 (just the two non-NaN values are used to compute the mean (3+3)/2)

```python
# ---- pandas solution

df = pd.DataFrame({'group': list('aabbabbbabab'),
                   'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})

# 1. Group by 'group'
# 2. Select the 'value' column
# 3. Apply a rolling window of 3
# 4. min_periods=1 allows the window to calculate even if 1 or 2 values are NaN
g1 = df.groupby(['group'])['value']
result = g1.rolling(3, min_periods=1).mean()

# The rolling operation on GroupBy returns a MultiIndex (group, original_index)
# We sort by the second level of the index to return to original order
result = result.reset_index(level=0, drop=True).sort_index()

print(result)
```

```python
# ------ polars  solution

pldf = pl.DataFrame({'group': list('aabbabbbabab'),
                   'value': [1, 2, 3, None, 2, 3, None, 1, 7, 3, None, 8]})

# 1. We use the rolling_mean expression
# 2. window_size=3
# 3. min_periods=1 (same logic as pandas)
# 4. .over("group") ensures the window doesn't leak across different groups
result = pldf.select(
    pl.col("value").rolling_mean(window_size=3, min_samples=1).over("group")
)

result.to_series()
```

