**N-Queen Solver (Python)**

Two Python implementations of the classic N-Queens solver (imperative and functional) plus a small comparator that reports solutions, runtime, and peak memory.

---

## What’s Inside
- `imperative.py` — Backtracking, in-place arrays for columns/diagonals; time/memory helpers.
- `functional.py` — Recursive functional style returning solution lists; time/memory helpers.
- `compare.py` — Interactive CLI that runs both implementations for a given `N`, prints the last solution as an ASCII board, and compares runtime and peak memory.

Requires Python 3.x only (standard library; uses `tracemalloc` for memory).

---

## Quick Start
From the repo root:
```bash
python compare.py
```
Enter a value for `N` (e.g., `8`). The script will:
- Run both implementations
- Print the last solution as an ASCII board
- Show timing, peak memory, solution count, and which approach was faster

---

## Key Functions
- `solve_imperative(n)` in `imperative.py`: list of solutions (each solution is a list of column indices per row).
- `time_imperative(n)` / `memory_imperative(n)`: measure runtime and peak memory for the imperative solver.
- `solve_functional(n)` in `functional.py`: list of solutions (tuples converted to lists).
- `time_functional(n)` / `memory_functional(n)`: measure runtime and peak memory for the functional solver.

---

## Example (`N=8`)
- Both implementations find 92 solutions. The ASCII board for the last solution will look similar to:
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
Then the script prints timing, peak memory, and which implementation was faster.

---

## Performance Notes
- Imperative version uses less memory and is typically faster for larger `N` because it updates state in-place.
- Both versions store all found solutions; for large `N`, memory can dominate. If you only need counts, avoid storing every solution.

---


