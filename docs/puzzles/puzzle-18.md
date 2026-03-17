# Puzzle  18.
 Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

```python
# ----  pandas solution
df.sort_values(by=['age', 'visits'], ascending=[False, True])
```

```python
# ----  polars solution
pldf.sort(["age", "visits"], descending=[True, False])
```

> Quick mental note: Pandas' sort_values() uses the ascending= parameter while polars' sort() used descending=

> We have introduced the polars [.sort()](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html) dataframe method here 

