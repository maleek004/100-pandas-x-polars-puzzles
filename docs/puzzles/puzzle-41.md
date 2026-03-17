# Puzzle 41. 
Delete the From_To column from **41.** Delete the **From_To** column from `df` and attach the temporary DataFrame 'temp' from the previous questions.`df` and attach the temporary DataFrame from the previous questions.

```python
# ------ pandas solution
# 1. Drop the original 'From_To' column
df = df.drop('From_To', axis=1)

# 2. Concatenate the original df and the temp df along the columns axis (axis=1)
df = pd.concat([df, pd_temp], axis=1)
df
```

```python
# ------ polars  solution
# 1. Drop 'From_To'
# 2. Use hstack to attach all columns from 'temp'
pldf = pldf.drop("From_To").hstack(pl_temp)

pldf
```

* Axis Alignment: In Pandas, axis=1 is the critical argument for both .drop() and pd.concat() to ensure you are operating on columns rather than rows.

* HStack vs Concat: Polars uses hstack (horizontal stack) as a convenient shorthand for gluing DataFrames together side-by-side without needing a complex library-level concat function.

* Side Effects: Pandas .drop() returns a copy by default; to modify the original without reassignment, you would need inplace=True (though reassignment is generally preferred).

* Selection Logic: Another common pattern in Polars is to simply select the columns you want to keep and add the new ones in a single chain, avoiding the "delete-then-attach" dance.

