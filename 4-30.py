import numpy as np
from scipy.optimize import linprog

c = [-350, -120, 0, 0]

A_eq = [[8, 2, 1, 0], [12, 5, 0, 1]]

b_eq = [1200, 1850]

result = linprog(c, A_eq=A_eq, b_eq=b_eq)

if result.success:
    print("Optimization was successful.")
    for i in range(4):
        print(f"Optimal value for x_{i+1}: {result.x[i]:.1f}")
else:
    print("Optimization failed.", result.message)