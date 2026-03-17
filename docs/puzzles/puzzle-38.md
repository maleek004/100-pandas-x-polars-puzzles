# Puzzle 38. 
Some values in the the **FlightNumber** column are missing (they are `NaN`). These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Modify `df` to fill in these missing numbers and make the column an integer column (instead of a float column).

```python
# ----- pandas solution
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})
                
# 1. Interpolate the missing values
# 2. Convert to integer (interpolation results in floats)
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

print(df[['FlightNumber']])
```

```python
# ------ polars solution
pldf = pl.DataFrame({
    'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
    'FlightNumber': [10045, None, 10065, None, 10085],
    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']
})

# 1. Cast to Float (interpolation requires floating point math)
# 2. Interpolate nulls
# 3. Cast back to Int64
result = pldf.with_columns(
    pl.col("FlightNumber").cast(pl.Float64).interpolate().cast(pl.Int64)
)

print(result.select("FlightNumber"))
```

* Linear Gaps: Both libraries use interpolate(), which assumes a linear progression between known points to fill the NaN or null values.

* Type Strictness: Polars requires numeric columns to be floats to perform interpolation math, whereas Pandas handles the transition from float (due to NaN) more implicitly.

* Integer Casting: Since missing value markers (NaN in Pandas) force columns to become floats, an explicit .astype(int) or .cast(pl.Int64) is required to return to whole numbers.

* Null Handling: Polars uses None for missing data, while Pandas traditionally uses np.nan (though it now supports a native pd.NA).

