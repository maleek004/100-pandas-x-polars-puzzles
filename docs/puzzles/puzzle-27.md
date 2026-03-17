# Puzzle 27. 
A DataFrame has a column of groups 'grps' and and column of integer values 'vals': 

```python
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
```
For each *group*, find the sum of the three greatest values. You should end up with the answer as follows:
```
grps
a    409
b    156
c    345
```

```python
# ------ pandas solution

df = pd.DataFrame({
    'grps': list('aaabbcaabcccbbc'), 
    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]
})

# 1. Group by 'grps'
# 2. Select 'vals' column
# 3. Use nlargest(3) to get top values per group
# 4. Sum the results per group
result = df.groupby('grps')['vals'].nlargest(3).groupby(level=0).sum()

print(result)
```

```python
# ------ polars solution
pldf = pl.DataFrame({
    'grps': list('aaabbcaabcccbbc'), 
    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]
})

# 1. Group by 'grps'
# 2. Inside each group: sort 'vals' descending, take the first 3, and sum them
result = (
    pldf.group_by("grps")
    .agg(
        pl.col("vals").sort(descending=True).head(3).sum()
    )
    .sort("grps")
)

print(result)
```

