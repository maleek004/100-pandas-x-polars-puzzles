# Immutability in Polars

One of the biggest paradigm shifts when moving from Pandas to Polars is understanding **immutability**.

## Pandas: In-Place Mutations
In Pandas, DataFrames are mutable. You can easily change a single value using row and column indexers like `.loc[]` or `.iloc[]`:

```python
# Pandas
df.loc["f", "age"] = 1.5
```
While convenient, mutating state in-place can lead to unintended side effects, unpredictable states in parallel execution, and `SettingWithCopyWarning`s.

## Polars: Expression-Based Replacements
Polars DataFrames are **immutable**. This means you are not supposed to modify them in place. Instead, you create a new DataFrame (or overwrite the variable) with the desired changes applied.

To change a value in Polars, you use `with_columns` combined with conditional expressions like `pl.when().then().otherwise()`:

```python
# Polars
pldf = pldf.with_columns(
    pl.when(pl.col("index") == "f")
    .then(1.5)
    .otherwise(pl.col("age"))
    .alias("age")
)
```

### Why is this better?
1. **Thread Safety**: Immutability makes parallel execution safe. Multiple threads can read the same DataFrame without worrying about another thread modifying it.
2. **Predictable Query Planning**: Since the data doesn't change unexpectedly, Polars' lazy query engine can confidently reorder and optimize operations.
3. **Lazy Execution Support**: The square bracket assignment `pldf[row, col] = value` is technically possible in Polars for interactive convenience, but **it will not work in Lazy mode**. The `with_columns` pattern works universally.
