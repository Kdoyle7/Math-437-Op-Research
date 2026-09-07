import numpy as np
from scipy.optimize import linprog

c = [-30, -20, -50]

A = [
    [-1, -1, -1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1],
    [1, 0.5, 0.333],
    [2, 3, 5],
    [4, 2, 7],
]

b = [0, -200, -200, -150, 1500, 4000, 6000]

Aeq = [[2, -3, 0], [0, 5, -2]]
beq = [0, 0]
res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method="highs")
z = 30 * res.x[0] + 20 * res.x[1] + 50 * res.x[2]
if res.success:
    print("Optimization was successful.")
    print(f"Maximum profit= {z:.1f}")
    for i in range(3):
        print(f"Optimal value for x_{i+1}: {res.x[i]:.1f}")
else:
    print("Optimization failed.", res.message)
