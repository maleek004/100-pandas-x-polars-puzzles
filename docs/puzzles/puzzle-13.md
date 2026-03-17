# Puzzle 13. 
Change the age in row 'f' to 1.5.

```python
# ----  pandas solution

df.loc["f","age"] = 1.5
```

> this is the puzzle where you understand why you should avoid chained indexing. Assuming we had written this instead `df.loc["f"].loc["age"] = 1.5` or `df.loc['f']['age'] = 1.5` or `df[5:6]["age"] = 1.5` then we would have gotten a `SettingWithCopyWarning` warning, BUT our notebook run will not stop running, which could introduce silent error to our whole process

```python
# ----  polars solution
pldf = pldf.with_columns(
    pl.when(pl.col("index") == "f")
    .then(1.5)
    .otherwise(pl.col("age"))
    .alias("age")
)

pldf

# Alternate, not recommened approach
#  -->  pldf[5,"age"] = 1.5  # Did we just sliced a polars dataframe using a row index again ???
```

> You might be wondering why the long method was the preferred approach when we have a shorter alternative. 

> First off, polars dataframes are immutable, this means we are 'not supposed to be able to' change them in place using an assignment operation like in pandas.

> Because of this, the 'only' way to change a cell in both a polars dataframe and lazyframe  will be to use the with_columns() method to create a new column with the updated cell

> But looking at the alternative solution above, apparently you could still change a polars dataframe in place using squared brackets. But this 'Square Bracket Assignment' feature was addad as a "convenience feature" for interactive work and ***it will not work on a lazyframe*** . So in short you should not get used to it, just know that it exists for your convenience in certain situations


