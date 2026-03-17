# Puzzle 21. 
For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (*hint: use a pivot table*).

```python
# ----  pandas solution
df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
```

```python
# ----  polars  solution
pldf.pivot(values="age", index="animal", on="visits", aggregate_function="mean")
```

[`.pivot()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.pivot.html#polars.DataFrame.pivot) (datafrane Method): A complex reshape operation that turns unique values of one column into new column headers.

Bonus Method that i haven't but is inportnt for any polars fundamentals material:
> [`.alias()`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.alias.html#polars.Expr.alias) : an expression method that Renames the expression.

