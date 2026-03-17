# Puzzle 25. 
How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)? As input, use a DataFrame of zeros and ones with 10 rows and 3 columns.

```python
df = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
```

```python
# ---- pandas solution
df = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))

# 1. Drop duplicate rows
# 2. Get the number of rows remaining
unique_row_count = len(df.drop_duplicates())

print(f"Number of unique rows: {unique_row_count}")
```

```python
# ------ polars solution
pldf = pl.from_pandas(df)

# 1. Keep only unique rows
# 2. Get the height (number of rows)
unique_row_count = pldf.unique().height

print(f"Number of unique rows: {unique_row_count}")
```

