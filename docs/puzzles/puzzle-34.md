# Puzzle 34. 
Find the sum of the values in series `s` for every Wednesday.

```python
# ----  pandas solution

# 1. Access the weekday property of the index (Monday=0, Wednesday=2)
# 2. Filter and sum
wednesday_sum = s[s.index.weekday == 2].sum()

print(f"Sum of values on Wednesdays: {wednesday_sum}")
```

```python
# ----  polars solution 
# 1. Filter the 'date' column where the weekday is 3 (Polars uses 1-7, Mon-Sun)
# 2. Select the 'vals' column and sum
wednesday_sum = pldf.filter(pl.col("date").dt.weekday() == 3).select(pl.col("vals").sum()).item()

print(f"Sum of values on Wednesdays: {wednesday_sum}")
```

> Direct Access: Pandas allows direct attribute access through the index (e.g., s.index.weekday), making it very concise for Series.

> The Namespace: Polars requires the .dt namespace to access datetime-specific functions like weekday() on a column.

> Integer Mapping: Note the numbering difference: Pandas defaults to Monday=0, while Polars defaults to Monday=1.

> Scalar Extraction: To get a single number out of a Polars result, we use .item(), whereas Pandas returns a scalar directly from the sum.

