# python  weekday.py
# Author: Andras Csullog 

# Write a program that outputs whether or not today is a weekday
# An example of running this program on a Thursday is given below:
# Yes, unfortunately today is a weekday.
# An example of running it on a Saturday is as follows:
# It is the weekend, yay!

# Importing the date library for using at calculating the today's date as a number
import datetime
from datetime import date

# Calculated the iso weekday will assign each day of the wekk as number: e.g. Monday = 1 , Tueasday = 2 , etc.
today = date.today().isoweekday

# Defining the numbers of week days in an array
weekDays = [1,2,3,4,5]

# If today's number equals one of the weekdays numbers, then print weekday:
if today == weekDays :
    print("Yes, unfortunately today is a weekday.")
# Otherwise print a weekend:    
else :
    print("It is the weekend, yay!")
    

# Used references:
# https://pythontic.com/datetime/date/weekday
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# https://poopcode.com/check-day-weekday-weekend-python/