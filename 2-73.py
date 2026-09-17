import numpy as np
from scipy.optimize import linprog

c=[-35,-150,-200,-230,0,0]

A = [
    [1,0,0,0,0,0],
    [-1,-1,-1,-1,0,0],
    [0,0,0,0,-1,-1]
]

b = [400, 25, 0]

A_eq = [
    [0,1,0,0,1,0],
    [0,0,1,0,-.8,1],
    [0,0,0,0,-.95,0]
]
b_eq = [1200, 0, 0]

result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, method='highs')

if result.success:
    print("Optimization was successful.")
    for i in range(6):
        print(f"Optimal value for x_{i+1}: {result.x[i]:.1f}")
else:
    print("Optimization failed.", result.message)