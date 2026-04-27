# The Absence of Row Indices

A fundamental structural difference between Pandas and Polars is how they identify rows.

## Pandas: First-Class Index
Pandas has a built-in `Index` (and `MultiIndex`) that sits alongside your data columns. Every row has a label (which can be integers, dates, or strings).
Operations in Pandas often rely on **index alignment**—meaning Pandas will match rows based on their index labels before combining them.

```python
# Pandas creates an index implicitly or explicitly
df = pd.DataFrame(data, index=['a', 'b', 'c'])
```

## Polars: No Row Index
Polars **does not maintain a persistent row index**. A Polars DataFrame is strictly a collection of columns (Series) of the same length. Rows have no inherent identity.

If you need a row identifier, you must add it explicitly as a standard column:
```python
# Polars
pldf = pl.DataFrame(data).with_columns(
    pl.Series("index", ['a', 'b', 'c'])
)
```

### Why did Polars drop the index?
1. **Performance**: Managing and aligning indices is computationally expensive. Dropping it removes significant overhead.
2. **Simplicity**: No index means no confusing `.reset_index()`, `.set_index()`, or `.loc` vs `.iloc` complexities.
3. **Database Philosophy**: Polars treats data more like a SQL database table, where row order is handled by explicit sorting and grouping, rather than inherent row labels.
