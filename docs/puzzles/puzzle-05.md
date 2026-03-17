# Puzzle  5 
Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

```python
# ---- pandas solution
df.describe()
```

```python
# ---- polars solution

pldf.describe()
```

```python
pldf.null_count()
```

> the `.info()` method [does not exist](https://github.com/pola-rs/polars/issues/2429) for the polars dataframe 

> If you want a polars equivalent to pandas' `df.info()` use `df.null_count()`

> Note that we had 2 `np.nan` in the age column from the dictionary that was used to create our dataframes, but when you look at the result of `describe()` (or `null_count()`) for the polars dataframe there were no null values detected... 

> This is because polars actually doesn't recognize numpy's `np.nan` as null, instead it sees it as an 'unknown float' 

> But, it instead recognizes `None` as null. 

> So to prevent this, we could have created a different dataset dictionary from which the polars dataframe will be created, and using `None` to represent null instead of `np.nan` like this : 
``` python
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, None, 5, 2, 4.5, None, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```
> Or we could manually manipulate the column to replace nan with `None` like below

```python
pldf = pldf.with_columns(
	pl.when(pl.col("age").is_nan())
	  .then(pl.lit(None).cast(pl.Float64))
	  .otherwise(pl.col("age"))
	  .alias("age")
)
pldf.describe()
```

