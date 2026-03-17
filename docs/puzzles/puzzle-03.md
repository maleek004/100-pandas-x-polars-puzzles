# Puzzle 3

Print out all the *version* information of the libraries that are required by pandas and polars.

```python
# ---- pandas solution
pd.show_versions()
```

```python
# ---- polars solution
pl.show_versions()
```

> Both Pandas and Polars expose `__version__` and `show_versions()` as part of common Python library conventions. 

> `__version__` follows a long-standing Python convention for identifying library releases.  

> `show_versions()` provides a snapshot of the runtime environment, which is essential for debugging data-related issues in real-world systems. ***basically, with `show_versions()` you will see both the pandas/polars version + a full list of its optional dependencies***

