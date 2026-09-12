import numpy as np
from scipy.optimize import linprog

c = [30, 30, 30, 28, 28, 28, 0.9, 0.9, .75, .75]

A = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [.75, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, .75, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, .75, 0, 0, 1, 0, 0, 0, 0],
]

b = [0, 3000, 3500, 3000]

Aeq = [
    [1, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, -1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
]

beq = [500, 5000, 750, 1000, 1200, 1200]

res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method="highs")


if res.success:
    print("Optimization was successful.")
    for i in range(10):
        print(f"Optimal value for x_{i+1}: {res.x[i]:.1f}")
else:
    print("Optimization failed.", res.message)
