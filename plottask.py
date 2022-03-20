# Week 08 Task
# Author: Andras Csullog

# Write a program called plottask.py that displays a plot of the functions 
# f(x)=x, 
# g(x)=x2 and 
# h(x)=x3 
# in the range [0, 4] on the one set of axes. 

import matplotlib.pyplot as plt 
import numpy as np

x = np.array(range(0,4))
y = x * x
z = x * x * x

plt.title ("Week 08 Task")
plt.plot (x, x, label = "f(x)")
plt.plot(x, y, label = "g(x)")
plt.plot (x, z, label = "h(x)")
plt.legend ()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()

# Used or chcked references:
# https://matplotlib.org/3.5.1/tutorials/introductory/pyplot.html
# https://stackoverflow.com/questions/18176591/importerror-no-module-named-matplotlib-pyplot 
# https://www.southampton.ac.uk/~fangohr/teaching/python/book/html/16-scipy.html
# https://www.w3schools.com/python/matplotlib_plotting.asp
# https://pythonprogramming.net/legends-titles-labels-matplotlib-tutorial/
# https://stackoverflow.com/questions/44813601/how-to-set-x-axis-values-in-matplotlib-python
# https://www.geeksforgeeks.org/how-to-set-x-axis-values-in-matplotlib-in-python/
# https://www.w3schools.com/python/matplotlib_grid.asp
