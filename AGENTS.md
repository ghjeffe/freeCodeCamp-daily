# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

A collection of Python coding exercises from freeCodeCamp, worked on collaboratively as a learning project.

## Structure

Each exercise lives in its own directory with a `main.py` entry point:
- `knight_moves/` - Chess knight move calculator
- `leap year calculator/` - Leap year determination
- `tire_pressure/` - Tire pressure status checker
- `vowelcase/` - Vowel/consonant case converter
- `odd or even day/` - (In progress)

## Running Code

```bash
python <exercise_dir>/main.py
```

Example:
```bash
python knight_moves/main.py
```

## Code Style

- Python 3.10+ (uses modern type hints like `list[str]`)
- Functions include docstrings with `:param`, `:type`, `:return`, `:rtype` format
- Each exercise is self-contained with inline test cases at the bottom of `main.py`
