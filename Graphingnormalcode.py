import matplotlib.pyplot as plt
import numpy as np

xmin = -3.0
xmax = 3.0
xstep = 0.01

sigma = 1.0
mu = 0.0

x = np.arange(xmin, xmax, xstep)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2 / (2 * sigma**2)))

fig, ax = plt.subplots(nrows=1, ncols=1)

ax.set(xlabel = 'x-axis', ylabel = 'y-axis', 
       title = f'Normal curve with mean {mu} and standard deviation {sigma}')

ax.grid()

ax.plot(x,y)
plt.show()