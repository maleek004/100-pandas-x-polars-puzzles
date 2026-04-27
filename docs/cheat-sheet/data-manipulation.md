# Data Manipulation Cheat Sheet

A quick mapping of common data modification tasks.

| Action | Pandas | Polars |
| :--- | :--- | :--- |
| **Replace value conditionally** | `df.loc[df['a'] == 1, 'b'] = 2` | `df.with_columns(pl.when(pl.col('a') == 1).then(2).otherwise(pl.col('b')).alias('b'))` |
| **Drop a column** | `df.drop('a', axis=1)` | `df.drop('a')` |
| **Rename a column** | `df.rename(columns={'a': 'b'})` | `df.rename({'a': 'b'})` |
| **Check for nulls** | `df.isna()` | `pl.col('a').is_null()` |
| **Expand list to columns** | `df['col'].apply(pd.Series)` | `df.select(pl.col('col').list.to_struct().unnest())` |
| **Create new column** | `df['c'] = df['a'] + df['b']` | `df.with_columns((pl.col('a') + pl.col('b')).alias('c'))` |
