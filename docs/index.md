# 100 Pandas x Polars Puzzles

Welcome to **100 Pandas x Polars Puzzles**! 

Inspired by [100 Pandas Puzzles](https://github.com/ajcr/100-pandas-puzzles) by Alex Riley, this project contains short data manipulation puzzles solved side-by-side in **Pandas** and **Polars**.

This is designed for people who are familiar with pandas and want to adopt polars to reap the performance and simplicity benefits that it offers.

## Why Polars?

- **Fast & Parallel**: Polars utilizes all available cores on your machine, unlike pandas which mostly uses a single core.
- **Query Optimization**: Polars supports a **LazyFrame** API that builds a query plan and optimizes the entire plan before execution.
- **Handles Large Datasets**: Polars can process datasets larger than your available RAM.
- **Consistent API**: Polars emphasizes explicit, expression-based transformations.
- **Strict Schema**: Polars enforces known data types before query execution, reducing data type surprises and bugs.

Check out the [Getting Started Overview](getting-started/overview.md) or dive right into the [Puzzles](puzzles/puzzle-01.md).
