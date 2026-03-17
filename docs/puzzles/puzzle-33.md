# Puzzle 33 - 43

## Series and DatetimeIndex

### Exercises for creating and manipulating Series with datetime data

Difficulty: *easy/medium*

pandas is fantastic for working with dates and times. These puzzles explore some of this functionality.

## Puzzle 33. 
Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers. Let's call this Series `s`.

```python
# ----  pandas  solution
# 1. Create the DatetimeIndex for business days in 2015
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')

# 2. Create the Series with random numbers indexed by those dates
s = pd.Series(np.random.rand(len(dti)), index=dti)

print(s.head())
print(f"\nTotal business days in 2015: {len(s)}")
```

```python
# ----  polars solution

from datetime import date

# 1. Generate every day in 2015
# 2. Filter for business days (Monday=1, ..., Friday=5)
# 3. Add a column of random values
pldf = (
    pl.date_range(date(2015, 1, 1), date(2015, 12, 31), interval="1d", eager=True)
    .alias("date")
    .to_frame()
    .filter(pl.col("date").dt.weekday() < 6) # 6 and 7 are Saturday/Sunday
    .with_columns(
        vals = pl.lit(np.random.rand(261)) # 261 is the count of B-days in 2015
    )
)

print(pldf.head())
```

> Indexing Differences: Again Pandas attaches dates as a metadata Index , whereas Polars treats dates as a standard data column since it lacks a built-in index.

> Function Similarity: Both libraries provide a **date_range** function to generate sequences of time points.

> Calendar Awareness: Pandas is "calendar-aware" out of the box; it uses [offset aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases) like freq='B' which handles business day logic automatically.

> Explicit Logic: Polars requires an explicit .filter() step (e.g., checking weekday) to achieve the same result as a Pandas offset alias.


