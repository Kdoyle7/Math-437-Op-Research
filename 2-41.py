import numpy as np
from scipy.optimize import linprog

# Maximizing y_5 by minimizing -y_5
c= [0, 0, 0, 0, 0, 0, 0, 0, -1] 

A=[
   [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
   [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
]

b=[0.0, 10000.0]

Aeq=[
    [.5,.6,-1,.4,1.065,-1,0,0,0],
    [.3,.2,.8,.6,0,1.065,-1,0,0],
    [1.8,1.5,1.9,1.8,0,0,1.065,-1,0],
    [1.2,1.3,.8,.95,0,0,0,1.065,-1],
    [2,-3,0,0,0,0,0,0,0],
    [0,5,-2,0,0,0,0,0,0],
]

beq=[0,0,0,0,0,0]



res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

if res.sucess:
    print("Optimazation was successful.")
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