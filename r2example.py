# first import the necessary libraries
import matplotlib
import numpy as np
import pandas as pd
import os
import tabulate
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')



# here is the  1.69
x = [1.69, 1.4835, 1.3195, 1.1355, 0.928, 0.81, 0.652, 0.465]
y = [481.6, 647.8, 779.8, 927.9, 1061.7, 1194.1, 1306.9, 1457.1]

r2 = np.corrcoef(x, y)[0, 1] ** 2

# plot the data as a scatter plot
plt.scatter(x, y)
# x label = Averaged Velocity (mm/s)
plt.xlabel('Average Velocity (mm/s)')
# y label = Averaged Force (N)
plt.ylabel('Average Force (N)')

# draw a linear regression line through the data
plt.plot(x, y, 'o', label='original data')

# linear regression, extrapolate to 0
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# x2 is 0 to the intercep of 0 on the line
x2 = np.linspace(0, -p[0] / p[1], 10)

y2 = p(x2)
plt.plot(x2, y2, 'k-', label='original data fit')

# axis limit is 0 to 1.1 times the intercep of 0 on the line
plt.xlim(0, 1.1 * -p[0] / p[1])
plt.ylim(0, 1.1 * p[0])




# title = Force vs. Velocity
plt.title('Force vs. Velocity')

# plot an regression line through x[5:6] and y[5:6]
plt.plot(x[4:6], y[4:6], 'x', label='narrow data')
z = np.polyfit(x[4:6], y[4:6], 1)
p = np.poly1d(z)
x2 = np.linspace(0, -p[0] / p[1], 10)
y2 = p(x2)
plt.plot(x2, y2, 'r--', label='narrow data fit')

# add the r^2 value to the plot
plt.text(0.05, 0.95, 'r^2 = ' + str(round(r2, 2)), transform=plt.gca().transAxes, fontsize=14)
plt.legend()
plt.show()

#%%
