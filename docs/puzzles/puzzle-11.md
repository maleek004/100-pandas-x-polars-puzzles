# Puzzle  11.
 Select the rows where the animal is a cat *and* the age is less than 3.

```python
# ----  pandas solution
df[(df.animal=='cat') & (df.age< 3)]
# remember that Pandas does not like multiple conditions without parentheses separating them
```

```python
# ----  polars  solution
pldf.filter((pl.col("animal") == "cat") & (pl.col("age") < 3))
```

