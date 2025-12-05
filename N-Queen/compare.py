import tracemalloc
from imperative import time_imperative, solve_imperative,memory_imperative
from functional import time_functional, solve_functional,memory_functional



def draw_board(solution):
    n = len(solution)
    board = []
    for r in range(n):
        row = []
        for c in range(n):
            if solution[r] == c:
                row.append("Q")   
            else:
                row.append(".")   
        board.append(" ".join(row))
    return "\n".join(board)



def show_solutions(title, solutions):
    print(f"\n      {title} Last Solution      ")

    sol = solutions[-1]       
    print(f"\nLast Solution: {sol}")
    print(draw_board(sol))
   


def compare(n):

    print(f"\n       Comparing For N = {n}       \n")

    imp_time, imp_count = time_imperative(n)
    fun_time, fun_count = time_functional(n)

    
    imp_solutions = solve_imperative(n)
    fun_solutions = solve_functional(n)
    
    show_solutions("Imperative", imp_solutions)
    show_solutions("Functional", fun_solutions)

    imp_peak=memory_imperative(n)
    fun_peak=memory_functional(n)
   
    print("\n     Performance Results     \n")

    print(f"Imperative Solutions : {imp_count}")
    print(f"Imperative Time      : {imp_time:.6f} sec")
    print(f"Imperative Peak Memory: {imp_peak} bytes\n")

    print(f"Functional Solutions : {fun_count}")
    print(f"Functional Time      : {fun_time:.6f} sec")
    print(f"Functional Peak Memory: {fun_peak} bytes\n")


    diff = abs(imp_time - fun_time)
    print(f"Time Difference = {diff:.6f} sec")

    if imp_time < fun_time:
        print("→ Imperative is Faster")
    elif fun_time < imp_time:
        print("→ Functional is Faster")
    else:
        print("→ Same Speed")

if __name__ == "__main__":
    n = int(input("Enter N: "))
    compare(n)
