# Weel 08 Task
# Author: Andras Csullog

# Write a program called plottask.py that displays a plot of the functions 
# f(x)=x, 
# g(x)=x2 and 
# h(x)=x3 
# in the range [0, 4] on the one set of axes. 

import matplotlib.pyplot as plt
import numpy as np

fpoints = np.array(range(0,4)) 
gpoints = fpoints * fpoints 
hpoints = fpoints * fpoints * fpoints

plt.plot(fpoints, gpoints, hpoints)
plt.show()

# Used or chcked references:
# https://matplotlib.org/3.5.1/tutorials/introductory/pyplot.html
# https://stackoverflow.com/questions/18176591/importerror-no-module-named-matplotlib-pyplot 
# https://www.southampton.ac.uk/~fangohr/teaching/python/book/html/16-scipy.html
# https://www.w3schools.com/python/matplotlib_plotting.asp
