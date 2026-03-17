# Puzzle 40. 
Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame 'temp'. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

```python
# ------ pandas solution
# Apply capitalization to both columns
pd_temp['From'] = pd_temp['From'].str.capitalize()
pd_temp['To'] = pd_temp['To'].str.capitalize()

pd_temp
```

```python
# ------ polars solution
# Apply to all columns in the 'temp' dataframe
pl_temp = pl_temp.with_columns(
    pl.all().str.to_titlecase()
)

pl_temp
```

* Consistency: Both libraries provide dedicated string methods to handle "Sentence Case" (Capitalizing the first letter and lowercasing the rest).

* Column-Wise vs. Bulk: In Pandas, you typically update columns one by one; in Polars, you can use pl.all() or pl.col(pl.String) to standardize every string column in the DataFrame at once.

* Namespace: Both use a string-specific namespace (.str) to access these specialized text-processing functions.

* In-place vs. Functional: Pandas often involves direct assignment (temp['col'] = ...), while Polars follows a functional pattern (with_columns) that returns a new modified DataFrame.

