import nbformat
import os
import re

NOTEBOOK_PATH = "notebooks/100-pandas-puzzles-solutions.ipynb"
OUTPUT_DIR = "docs/puzzles"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load notebook
with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

puzzles = []
current_puzzle = None

for cell in nb.cells:

    if cell.cell_type == "markdown":
        text = cell.source.strip()

        # Detect puzzle heading
        match = re.match(r"#\s*Puzzle\s*(\d+)", text, re.IGNORECASE)

        if match:
            # Save previous puzzle
            if current_puzzle:
                puzzles.append(current_puzzle)

            puzzle_number = int(match.group(1))

            current_puzzle = {
                "number": puzzle_number,
                "cells": []
            }

        if current_puzzle:
            current_puzzle["cells"].append(cell)

    else:
        if current_puzzle:
            current_puzzle["cells"].append(cell)

# Add last puzzle
if current_puzzle:
    puzzles.append(current_puzzle)

print(f"Found {len(puzzles)} puzzles")

# Convert puzzles to markdown files
for puzzle in puzzles:

    number = puzzle["number"]
    filename = f"puzzle-{number:02}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:

        f.write(f"# Puzzle {number}\n\n")

        for cell in puzzle["cells"]:

            if cell.cell_type == "markdown":
                f.write(cell.source + "\n\n")

            elif cell.cell_type == "code":
                f.write("```python\n")
                f.write(cell.source)
                f.write("\n```\n\n")

    print("Generated", filename)