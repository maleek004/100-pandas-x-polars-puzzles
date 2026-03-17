# Puzzle 36. 
For each group of four consecutive calendar months in `s`, find the date on which the highest value occurred.

```python
# ------ Pandas solution
s.groupby(pd.Grouper(freq='4ME')).idxmax()
```

```python
# ------ Polars  solution
# 1. Use group_by_dynamic with a 4-month window
# 2. Find the row (date) where 'vals' is at its maximum within that 4-month block
#result = pldf.group_by_dynamic("date", every="1mo", period="4mo").agg(
#    pl.col("date").sort_by("vals", descending=True).first()
#)

result = pldf.group_by_dynamic("date", every="1mo", period="4mo").agg(
    pl.col("date").sort_by("vals", descending=True).first().alias("max_val_date")
)

print(result.tail())
```

