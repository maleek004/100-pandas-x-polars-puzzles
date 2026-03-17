# Puzzle 39.
The **From\_To** column would be better as two separate columns! Split each string on the underscore delimiter `_` to give a new temporary DataFrame called 'temp' with the correct values. Assign the correct column names 'From' and 'To' to this temporary DataFrame. 

```python
# ------Pandas  solution
# 1. Split the string on '_'
# 2. expand=True returns a DataFrame instead of a Series of lists
pd_temp = df['From_To'].str.split('_', expand=True)

# 3. Assign column names
pd_temp.columns = ['From', 'To']

pd_temp
```

```python
# ------ Polars solution
# 1. Split the string into a Struct with specific field names
# 2. Unnest the struct to turn those fields into top-level columns
pl_temp = (
    pldf.select(
        pl.col("From_To")
        .str.split_exact("_", 1)
        .struct.rename_fields(["From", "To"])
    )
    .unnest("From_To")
)

pl_temp
```

* Expansion Logic: Pandas uses expand=True to jump directly from a Series to a DataFrame, while Polars uses a two-step process: creating a Struct and then unnest-ing it.

* Exact vs. General: Polars' split_exact is safer and faster because it forces you to specify how many splits you expect, preventing messy rows if an extra delimiter exists.

* Metadata Assignment: In Pandas, you rename columns by modifying the .columns attribute of the new object; in Polars, you define the names during the expression using rename_fields.

* Temporary Objects: Both methods result in a "Temporary" structure that is detached from the original DataFrame until you explicitly join or assign it back.

