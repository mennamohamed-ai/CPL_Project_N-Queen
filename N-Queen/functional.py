import time
import tracemalloc
from itertools import chain
def conflict(col, row, solution):
    for r, c in enumerate(solution):  # r=head(index), c=tail(value)
            if c == col or abs(c-col) == abs(r-row):#
              return True
    return False
    
def search(n, row, solution):               
    if row == n:
        return [solution]
    results = []
    # Higher-Order Functions
    valid_cols = filter(lambda c: not conflict(c, row, solution), range(n))
    results = list(chain.from_iterable(
        search(n, row + 1, solution + (col,))
        for col in valid_cols
    ))
    return results

def solve_functional(n):
    sols = search(n, 0, ())
    return [list(s) for s in sols]

def count_functional(n):
    return len(search(n, 0, ()))

def time_functional(n):
    start = time.time()
    s = solve_functional(n)
    end = time.time()
    return (end - start), len(s)

 
def memory_functional(n):
  tracemalloc.start()
  _ = solve_functional(n)
  fun_current, fun_peak = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  return fun_peak
