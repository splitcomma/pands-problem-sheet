# python  weekday.py
# Author: Andras Csullog 

# Write a program that outputs whether or not today is a weekday
# An example of running this program on a Thursday is given below:
# Yes, unfortunately today is a weekday.
# An example of running it on a Saturday is as follows:
# It is the weekend, yay!

from calendar import weekday
import datetime
from datetime import date
today = date.today()
print ("Today's date :", today)
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekend = ["Saturday","Sunday"]
if today == weekDays :
    print("Yes, unfortunately today is a weekday.")
elif today == weekend :
    print("It is the weekend, yay!")
