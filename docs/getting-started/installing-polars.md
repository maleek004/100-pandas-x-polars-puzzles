# Installing Polars

To get started with Polars, you'll need to install the library. It is available on PyPI and can be installed via `pip` or `conda`.

## Using pip

The standard installation command is:

```bash
pip install polars
```

If you plan to use Polars with legacy pandas or want to enable all optional features (like pyarrow for fast I/O, or fsspec for cloud storage), you can install all optional dependencies:

```bash
pip install polars[all]
```

## Using conda

If you use Conda, you can install Polars from the conda-forge channel:

```bash
conda install -c conda-forge polars
```

## Verify Installation

You can check if Polars is installed correctly and see your system details by running:

```python
import polars as pl
pl.show_versions()
```

This will print the Polars version along with information about any optional dependencies.
