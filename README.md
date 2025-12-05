**N-Queen Project**

**Overview:**
- **Purpose:**: This repository contains two implementations (imperative and functional) of a solver for the classic N-Queens problem and a small comparator script that measures and prints time, memory, and solution counts.
- **Language:**: Python 3.x (uses standard library only — `tracemalloc` for memory measurements).


**Repository Structure:**
- `imperative.py`: Imperative/backtracking implementation that solves N-Queens in-place using arrays for columns and diagonals. Provides functions to solve, count, measure time, and measure peak memory.
- `functional.py`: Functional-style recursive implementation that builds solutions as tuples and returns lists of solutions. Provides solve/count/time/memory helpers.
- `compare.py`: CLI entry that runs both implementations for a given `N`, prints the last found solution as an ASCII board, and compares time and peak memory usage.


**How to Run:**
- Run interactively from the repo root:

```bash
python compare.py
```

You will be prompted to enter a value for `N` (e.g. `8`). The script will run both implementations, print the last solution as an ASCII board, and display timing/memory statistics and which implementation was faster.


**Key Functions**
- `solve_imperative(n)` in `imperative.py`: returns a list of solutions (each solution is a list of column indices for each row).
- `time_imperative(n)` / `memory_imperative(n)`: measure execution time and peak memory for the imperative solver.
- `solve_functional(n)` in `functional.py`: returns a list of solutions (converted from tuples to lists).
- `time_functional(n)` / `memory_functional(n)`: measure execution time and peak memory for the functional solver.


**Example Output (when running `compare.py` with `N=8`)**
- Both implementations will find the known number of solutions for `N=8` (92). The script prints the last solution and an ASCII board like:

```
Q . . . . . . .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . . . Q . .
```

Then it prints timing, peak memory, and which approach was faster.


**Performance Notes & Observations:**
- The imperative implementation performs in-place updates and generally uses less memory and runs faster for larger `N` than the functional implementation, which creates new tuples/lists on each recursive call.
- Both approaches store all found solutions in memory; for large `N` this can become the limiting factor. If only the count is required, avoid storing full solution lists.


**Suggested Improvements / Next Steps:**
- Convert `compare.py` to a CLI using `argparse` so it can run non-interactively and accept options like `--min`, `--max`, `--csv` output.
- Add an option to `solve_*` to return an iterator/generator instead of storing all solutions (allow streaming solutions and reduce peak memory).
- Add unit tests (e.g., `tests.py`) for small `N` values to validate counts and example solutions.
- Use `time.perf_counter()` for higher-resolution timing and run multiple iterations to compute averages.
- Add a `bench.py` to run batch experiments for a range of `N` values and save results to CSV for analysis.






