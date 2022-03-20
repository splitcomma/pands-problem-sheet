#Week 6 task
# Estimating Square Root 
# Author: Andras Csullog

#create a function called <tt>sqrt</tt>
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

#Newton's square root equation:  √ N ≈ ½(N/A + A)


print("enter a loating point number")
n = float(input())
nestimate = n / 3
for x in range(6):
    a = ((n / nestimate) + nestimate)/2
    nestimate = a


print ("squareroot is:  {:.1f}" .format (a))


# Used references:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,to%20be%20N%20or%201.
# https://www.programiz.com/python-programming/for-loop
# https://www.school-for-champions.com/algebra/square_root_approx.htm#.YjcKgep_r4Z
