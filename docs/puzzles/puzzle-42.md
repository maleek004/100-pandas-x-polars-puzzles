# Puzzle 42. 
In the **Airline** column, you can see some extra puctuation and symbols have appeared around the airline names. Pull out just the airline name. E.g. `'(British Airways. )'` should become `'British Airways'`.

```python
# ------ pandas  solution

# Regex breakdown:
# [a-zA-Z\s]+  -> Match one or more letters or whitespace characters
# ([a-zA-Z\s]+) -> Capture that group
df['Airline'] = df['Airline'].str.extract(r'([a-zA-Z\s]+)', expand=False).str.strip()

df['Airline']
```

```python
# ------ Polars solution
# Using extract with a similar regex pattern
# index=1 refers to the first capture group
result = pldf.with_columns(
    pl.col("Airline")
    .str.extract(r"([a-zA-Z\s]+)", 1)
    .str.strip_chars()
)

result.select("Airline")
```

* Capture Groups: Using parentheses () in a regex pattern allows you to "capture" the specific part of the string you want to keep while ignoring the rest.

* Character Classes: The pattern [a-zA-Z\s] specifically targets lowercase letters, uppercase letters, and whitespace, effectively filtering out punctuation and numbers.

* Greedy Matching: The + symbol ensures we grab the longest possible string of letters (e.g., "British Airways") rather than just the first letter.

* Cleaning the Clean: After extracting, it’s common to run a strip() (Pandas) or strip_chars() (Polars) to remove any lingering whitespace at the start or end of the captured string.

