# Puzzle 19.
The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

```python
# ----  Pandas solution

df['priority'] = df['priority'].map({'yes': True, 'no': False})
df 

# Alternate approach
# -- df = df.assign(priority= df['priority'].map({'yes': True, 'no': False}))
```

```python
# ----  polars  solution
pldf.with_columns(pl.col("priority") == "yes")
```

