# Puzzle 37. 
Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016.

```python
# ------ Pandas solution
# 'WOM-3THU' = Week Of Month, 3rd Thursday
thursdays = pd.date_range('2015-01-01', '2015-12-31', freq='WOM-3THU')

print(thursdays)
```

```python
# ------polars solution
# thursdays = (
#     pl.date_range(date(2015, 1, 1), date(2015, 12, 31), interval="1d", eager=True)
#     .to_frame("date")
#     .filter(pl.col("date").dt.weekday() == 4) # Thursday
#     .group_by(pl.col("date").dt.month())
#     .agg(pl.col("date").sort().gather(2)) # Index 2 is the 3rd occurrence
#     .sort("date")
#     .explode("date")
#     .get_column("date")
# )

thursdays = (
    pl.date_range(date(2015, 1, 1), date(2015, 12, 31), interval="1d", eager=True)
    .to_frame("date")
    .filter(pl.col("date").dt.weekday() == 4) # Thursday
    .group_by(pl.col("date").dt.month())
    .agg(
        # We name this 'third_thursday' to avoid the DuplicateError
        pl.col("date").sort().gather(2).alias("third_thursday") 
    )
    .sort("third_thursday")
    .explode("third_thursday")
    .get_column("third_thursday")
)

thursdays
```

* what the hail is this name collission error that i keep running into ??

* Pre-baked Logic: Pandas has a deep library of "Offest Aliases" like WOM-3THU that encode complex calendar rules directly into the freq parameter.

* Filter and Gather: Polars requires a "First Principles" approach: filter for the weekday, group by the month, and then gather (pick) the specific ordinal occurrence (the 3rd one).

* Monday-Sunday Indexing: Remember the 1-based vs 0-based difference. In Polars, Thursday is 4. In Pandas, Thursday is 3.

* The "Explode" Step: When aggregating in Polars, the result is often a list. Using .explode() flattens those lists back into individual rows.

* Name Collision: In Polars, the column used in group_by is automatically carried over to the output. If your aggregation (agg) also produces a column with that same name, Polars throws a DuplicateError.

* The Alias Fix: Using .alias("new_name") inside the aggregation is the standard way to prevent name conflicts.

* Property Access: In Polars, dt.month() is used to extract the month integer for grouping, while Pandas would typically use df.index.month.

* Explicit Ordinals: While Pandas uses hidden calendar logic (WOM-3THU), Polars makes the logic explicit: find all Thursdays, group them by month, and "gather" the 3rd one (index 2).

