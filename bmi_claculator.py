# Week 2 Task Creating a BMI Calculator 
# Author: Andras Csullog

# Task descrition
# $ python bmi.py
# Enter weight(kg): 65
# Enter height(cm): 180
# The BMI is (kg/m2) 20.06.

print ("This is a BMI calculator")
kg = float(input("Please enter your weight in Kilograms:"))
cm = float(input("Enter height(cm):"))

bmi = kg / (cm / 100)**2
print ("Your BMI index is:  {:.1f}" .format (bmi))
