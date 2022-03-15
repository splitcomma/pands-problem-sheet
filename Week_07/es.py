#Week 7 task
# Reads in a text file and outputs the number of e'
# Author: Andras Csullog

# It should read in a text file and outputs the number of e'
# The program should take the filename from an argument on the command line.


file = open('Week_07\mobydick.txt', 'r')

mobiDick= file.read()

letter1 = 'e'
letter2 = 'E'

letterCount = mobiDick.count(letter1) + mobiDick.count(letter2)
print(letterCount)

 


# Used references:
