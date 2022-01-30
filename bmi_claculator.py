# Week 2 Task Creating a BMI Calculator 
# Author: Andras Csullog

# Task descrition
# $ python bmi.py
# Enter weight(kg): 65
# Enter height(cm): 180
# The BMI is (kg/m2) 20.06.

kg = input("Enter your weight in Kilograms:")
cm = input("Enter height(cm):")
bmi = int(kg) / int(cm)
print("Your BMI index is:{}" .format (bmi))