# Weel 04 Task
# Author: Andras Csullog

# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

#  Have the program end if the current value is one.
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1

positiveInteger = int (input ("Please enter a positive integer: "))
even = positiveInteger % 2 == 0

if even :
    print(int(positiveInteger/2))
else :
    print(int((positiveInteger*3)+1))

