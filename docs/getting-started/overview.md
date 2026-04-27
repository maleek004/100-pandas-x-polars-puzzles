# Getting Started Overview

If you are new to Polars, the best way to learn is by seeing how common Pandas operations translate to Polars.

## The Polars Philosophy

Polars follows a **functional, expression-based model** built around three core concepts:

1. **Constructors**: E.g., `pl.col()`, `pl.lit()`
2. **Expressions**: E.g., `.sum()`, `.is_between()`, `.replace()`
3. **Contexts**: E.g., `.select()`, `.filter()`, `.with_columns()`

Most work in Polars happens by combining **Expressions inside a Context**.
This allows Polars to analyze and optimize the full expression chain *before any data is processed* — one of the key reasons it performs so well.

## Eager vs Lazy Execution

Polars offers both:
- **Eager API (DataFrame)**: Executes immediately, similar to Pandas. Great for interactive exploration.
- **Lazy API (LazyFrame)**: Builds a query plan and executes only when an action like `.collect()` or `.fetch()` is called. This is faster and uses less memory.

In these puzzles, we primarily use the Eager API for interactive learning, though many solutions would be written identically in Lazy mode.
