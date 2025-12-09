import time
import tracemalloc

def conflict(col, row, solution):
    for r, c in enumerate(solution):  # r=head(index), c=tail(value)
            if c == col or abs(c-col) == abs(r-row):#
              return True
    return False

def search(n, row, solution):               
    if row == n:
        return [solution]
    results = []
    for col in range(n):
        if not conflict(col, row, solution):
            results += search(n, row+1, solution + (col,))# {0,2}
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
