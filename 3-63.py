import numpy as np
from scipy.optimize import linprog

c= [2, 3]

A=[
    [3, 2],
    [2, 6]
]

b=[8, 18]

result = linprog(c, A_eq=A, b_eq=b, method='highs') 

if result.success:
    print("Optimization was successful.")
    for i in range(2):
        print(f"Optimal value for x_{i+1}: {result.x[i]:.1f}")
else:
    print("Optimization failed.", result.message)