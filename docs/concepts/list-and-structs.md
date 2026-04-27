# Lists and Structs

When working with nested or variable-length data (like a column where each cell contains a list of items), Pandas and Polars take vastly different approaches.

## Pandas: Object Types and Apply
Pandas typically stores lists within columns as generic Python `object` types. To expand a list into multiple columns, Pandas relies on the `.apply(pd.Series)` trick:

```python
# Pandas
delays = df['RecentDelays'].apply(pd.Series)
```
This iterates over each row, treating the list as a row for a new DataFrame. It is flexible but **very slow** on large datasets.

## Polars: Typed Lists and Structs
Polars has first-class support for `List` data types. However, because DataFrames require a fixed schema, you cannot simply "explode" a list into an unknown number of columns dynamically. 

Instead, Polars uses **Structs**. A Struct is a logical grouping of columns. You convert the list to a struct, and then "unnest" it:

```python
# Polars
max_width = pldf["RecentDelays"].list.len().max()

delays_pl = (
    pldf.select(
        pl.col("RecentDelays")
        .list.to_struct(upper_bound=max_width)
    )
    .unnest("RecentDelays")
)
```

### Key Differences
- **Schema Enforcement**: Polars forces you to declare the `upper_bound` (the maximum number of columns expected). This ensures type safety and predictable schemas during parallel execution.
- **Memory Efficiency**: The Struct and Unnest pattern operates directly on the underlying memory arrays, making it orders of magnitude faster than Pandas' row-by-row `.apply()`.
