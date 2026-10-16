# DNA Sequence Analyzer

## Overview

A beginner Bioinformatics project written in Python to analyze DNA sequences.

## Features

- Validates DNA sequences and patterns.
- Counts the number of A, T, G, and C bases.
- Calculates GC content percentage.
- Searches for a DNA pattern and reports its starting positions.
- Handles empty DNA sequence input with a clear error message.

## Technologies

- Python 3

## Example

**Input:**
- DNA sequence: `ATGCA`
- Pattern: `TG`

**Expected output:**

```text
A: 2
T: 1
G: 1
C: 1
GC%: 40.0
1
```

The pattern `TG` is found at index `1` (zero-based indexing).

## How to Run

## How to Run

1. Install Python 3.
2. Open the Python file in Visual Studio Code.
3. Click **Run Python File** to start the program.
4. Enter a DNA sequence when prompted.
5. Enter a DNA pattern when prompted.
6. The program will display base counts, GC content, and pattern positions.
