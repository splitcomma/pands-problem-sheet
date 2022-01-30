# Week 2 Task Creating a BMI Calculator 
# Author: Andras Csullog

# Task descrition
# $ python bmi.py
# Enter weight(kg): 65
# Enter height(cm): 180
# The BMI is (kg/m2) 20.06.

print ("This is a BMI calculator")
# kg and cm created as float so I dont have to convert string to float in the actual bmi calculation step
kg = float(input("Please enter your weight in kilograms:"))
cm = float(input("Enter height(cm):"))
# formatted float to 1f precision to print single decimal digit 
bmi = kg / (cm / 100)**2
print ("Your BMI index is:  {:.1f}" .format (bmi))
