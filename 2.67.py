import numpy as np
from scipy.optimize import linprog

c= [-1.04,-1.15,-1.11]

A = [
    [.5,.25,0],
    [0,.25,.4],
    [.5,.5,.6],
    [-1,-1,-1]
]

b = [300000, 120000, 150000, 0]

result = linprog(c, A_ub=A, b_ub=b, method='highs')

if result.success:
    print("Optimization was successful.")
    for i in range(3):
        print(f"Optimal value for x_{i+1}: {result.x[i]:.1f}")
else:
    print("Optimization failed.", result.message)