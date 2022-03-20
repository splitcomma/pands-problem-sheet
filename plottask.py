# Weel 08 Task
# Author: Andras Csullog

# Write a program called plottask.py that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. 

import matplotlib.pyplot as plt
import math

x = [float(i)/100 for i in range(0, 628)]
y = [math.sin(z) for z in x]

plt.plot(x,y)

# Used or chcked references:
# https://matplotlib.org/3.5.1/tutorials/introductory/pyplot.html
#
#
