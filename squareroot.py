#Week 6 task
# Estimating Square Root 
# Author: Andras Csullog

#create a function called <tt>sqrt</tt>
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

#Newton's square root equation:  √ N ≈ ½(N/A + A)


#print(input("Enter a floating point number:"))

def sqrt(num, iter = 10):
    a = float (num)
    
    for x in range(iter):
        num = 0.5*(num + (a / num))
    return num
    
userNumber = float(input("Please Enter a Number: "))
print("The Square Root of: ", userNumber, " is {:.1f}".format(sqrt(userNumber)))

# Used references:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,to%20be%20N%20or%201.
# https://www.programiz.com/python-programming/for-loop
# https://www.school-for-champions.com/algebra/square_root_approx.htm#.YjcKgep_r4Z