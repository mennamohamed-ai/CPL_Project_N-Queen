import time
import tracemalloc
def solve_imperative(n):
    board = [-1] * n
    solutions = []
    col = [False] * n
    diag1 = [False] * (2*n)
    diag2 = [False] * (2*n)

    def backtrack(r):
        if r == n:
            solutions.append(board.copy())
            return
        for c in range(n):
            if col[c] or diag1[r+c] or diag2[r-c+n]:
                continue
            col[c] = diag1[r+c] = diag2[r-c+n] = True
            board[r] = c
            backtrack(r+1)
            col[c] = diag1[r+c] = diag2[r-c+n] = False

    backtrack(0)
    return solutions
def count_imperative(n):
    return len(solve_imperative(n))

def time_imperative(n):
    start = time.time()
    s = solve_imperative(n)
    end = time.time()
    return (end - start), len(s)

# قياس الذاكرة Imperative
def memory_imperative(n):
    tracemalloc.start()
    _ = solve_imperative(n)
    imp_current, imp_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return imp_peak