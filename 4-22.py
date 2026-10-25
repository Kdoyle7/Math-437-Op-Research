import numpy as np
from scipy.optimize import linprog

c = [2, 1, 0, 0, 0]

A_eq = [[3, 1, -1, 0, 0], [4, 3, 0, -1, 0], [1, 2, 0, 0, 1]]

b_eq = [3, 6, 3]

result = linprog(c, A_eq=A_eq, b_eq=b_eq)
if result.success:
    print("Optimization was successful.")
    for i in range(5):
        print(f"Optimal value for x_{i+1}: {result.x[i]:.1f}")
else:
    print("Optimization failed.", result.message)