# Puzzle  22 - 28

## DataFrames: beyond the basics

### Slightly trickier: you may need to combine two or more methods to get the right answer

Difficulty: *medium*

The previous section was tour through some basic but essential DataFrame operations. Below are some ways that you might need to cut your data, but for which there is no single "out of the box" method.

## Puzzle 22 
You have a DataFrame `df` with a column 'A' of integers. For example:
```python
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
```

How do you filter out rows which contain the same integer as the row immediately above?

You should be left with a column containing the following values:

```python
1, 2, 3, 4, 5, 6, 7
```

```python
# ----  pandas solution -- this is the 'deduplicating consecutive values' problem in data analytics , 
# which is different from deduplicating the whole column which your first instinct might tell you to
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
result = df.loc[df['A'].shift() != df['A'] ]
result
```

```python
# ----  polars solution
pldf = pl.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
result = pldf.filter(
    (pl.col("A") != pl.col("A").shift()).fill_null(True)
)
result
```

