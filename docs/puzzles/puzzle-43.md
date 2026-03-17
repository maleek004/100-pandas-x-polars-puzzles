# Puzzle 43. 
In the **RecentDelays** column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.

Expand the Series of lists into a new DataFrame named 'delays', rename the columns 'delay_1', 'delay_2', etc. and replace the unwanted RecentDelays column in `df` with 'delays'.

```python
# ------ Pandas solution

# 1. Expand the list column into a new DataFrame
delays = df['RecentDelays'].apply(pd.Series)

# 2. Rename columns using a list comprehension
delays.columns = [f'delay_{i+1}' for i in range(delays.shape[1])]

# 3. Drop the old column and join the new 'delays' DataFrame
df = df.drop('RecentDelays', axis=1).join(delays)

df
```

```python
# ------ Polars  solution
# 1. Determine the maximum length of the lists to set the "upper_bound"
max_width = pldf["RecentDelays"].list.len().max()

# 2. Convert to struct using the upper_bound and rename the fields
delays_pl = (
    pldf.select(
        pl.col("RecentDelays")
        .list.to_struct(upper_bound=max_width)
    )
    .unnest("RecentDelays")
)

# 3. Rename columns from "field_0", "field_1" to "delay_1", "delay_2"
delays_pl.columns = [f"delay_{i+1}" for i in range(len(delays_pl.columns))]

# 4. Attach back
pldf = pldf.drop("RecentDelays").hstack(delays_pl)

print(pldf)
```

* Series-to-DataFrame: In Pandas, .apply(pd.Series) is a "magic" trick that treats each list like rows of a new DataFrame, automatically handling varying lengths with NaN.

* List-to-Struct: Polars uses the .list.to_struct() pattern. Since DataFrames can't have "variable length" columns, converting to a Struct (fixed fields) and then unnest-ing is the standard workflow.

* Dynamic Column Naming: Both solutions use dynamic naming (list comprehensions or lambda functions) because the number of columns depends on the length of the longest list in the data.

* Memory Efficiency: Polars' approach is highly optimized for memory; Pandas' .apply(pd.Series) can be very slow on large datasets because it essentially iterates through every row.

* Schema Enforcement: Unlike Pandas, which calculates the shape "on the fly," Polars prefers to know the column count upfront. Setting upper_bound tells Polars the maximum number of columns to create from the lists.

* Struct Fields: By default, .list.to_struct() names columns field_0, field_1, etc. If you want specific names like delay_1, you must rename them after the unnesting or by passing a list of names to the fields argument.

* Exploding vs. Expanding: Note that we are expanding (adding columns) rather than exploding (adding rows). Exploding would create a new row for every element in the list, while expanding keeps one row per original entry.

* Type Safety: This explicit approach prevents "unpredictable results" where different chunks of data might otherwise result in different numbers of columns during parallel processing.

