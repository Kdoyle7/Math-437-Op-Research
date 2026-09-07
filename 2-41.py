import numpy as np
from scipy.optimize import linprog

c = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]

A = [
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
[1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
]

b = [0.0, 10000.0]

Aeq = [
[0.5, 0.6, -1, 0.4, 1.065, -1, 0, 0, 0],
[0.3, 0.2, 0.8, 0.6, 0, 1.065, -1, 0, 0],
[1.8, 1.5, 1.9, 1.8, 0, 0, 1.065, -1, 0],
[1.2, 1.3, 0.8, 0.95, 0, 0, 0, 1.065, -1],
]

beq = [0.0, 0.0, 0.0, 0.0]

res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method="highs")

if res.success:
    print("Optimization was successful.")
    print(f"optimal value for x_1: {res.x[0]:.1f}")
    print(f"optimal value for x_1: {res.x[1]:.1f}")
    print(f"optimal value for x_1: {res.x[2]:.1f}")
    print(f"optimal value for x_1: {res.x[3]:.1f}")
    print(f"optimal value for x_1: {res.x[4]:.1f}")
    print(f"optimal value for x_1: {res.x[5]:.1f}")
    print(f"optimal value for x_1: {res.x[6]:.1f}")
    print(f"optimal value for x_1: {res.x[7]:.1f}")
    print(f"optimal value for x_1: {res.x[8]:.1f}")
else:
    print("Optimization failed.", res.message)