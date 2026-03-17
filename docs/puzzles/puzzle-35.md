# Puzzle 35. 
For each calendar month in `s`, find the mean of values.

```python
# ------ Pandas  solution
s.resample('ME').mean()
```

```python
# --- polars  solution

# 1. group_by_dynamic uses the 'date' column
# 2. '1mo' tells Polars to create 1-month windows
monthly_means = pldf.group_by_dynamic("date", every="1mo").agg(
    pl.col("vals").mean()
)

print(monthly_means)
```

* You can also use the resample() on a dataframe if it has a date-time like ([DatetimeIndex](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html), [TimedeltaIndex](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html) or [PeriodIndex](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html)) index or column 

* Running the resample() method on a valid (ie contains a date-time like index ) object will only return an DatetimeIndexResampler object, to get some actual data back , you need to use an agregat method e.g `sum()`, `mean()` on it.. you will notice it behaved just like using the `groupby()` method well, it is "the groupby for timeseries data"

* the group_by_dynamic() method is polars equivalent of pandas .resample() .. its too is used to group a polars df based on a time column (or index value of type Int32, Int64)
    * it returns a DynamicGroupBym unless you run a .agg expression on it 

