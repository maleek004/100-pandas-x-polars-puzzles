# DataFrame Basics Cheat Sheet

A quick mapping of fundamental DataFrame operations.

| Action | Pandas | Polars |
| :--- | :--- | :--- |
| **Create from Dict** | `pd.DataFrame(data)` | `pl.DataFrame(data)` |
| **Get first N rows** | `df.head(N)` | `df.head(N)` |
| **Get last N rows** | `df.tail(N)` | `df.tail(N)` |
| **Summary statistics** | `df.describe()` | `df.describe()` |
| **Data types & nulls info** | `df.info()` | `df.schema` or `df.null_count()` |
| **Convert to Pandas** | - | `df.to_pandas()` |
| **Convert to Polars** | `pl.from_pandas(df)` | - |
