# Puzzle 24 
Suppose you have DataFrame with 10 columns of real numbers, for example:

```python
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
```
Which column of numbers has the smallest sum?  Return that column's label.

```python
# ---- pandas solution
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

# 1. Sum the columns (returns a Series)
# 2. Get the label of the minimum value
min_col_label = df.sum().idxmin()

print(f"The column with the smallest sum is: {min_col_label}")
```

```python
# ----- polars  solution

pldf = pl.DataFrame(np.random.random(size=(5, 10)), schema=list('abcdefghij'))

# 1. Sum all columns (returns a 1-row DataFrame)
# 2. Melt to turn column names into a 'variable' column
# 3. Sort by the sums and take the first column name
min_col_label = (
    pldf.sum()
    .unpivot()
    .sort("value")
    .item(0, "variable")
)

print(f"The column with the smallest sum is: {min_col_label}")
```

