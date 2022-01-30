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

# Bonus code for displaying BMI category based on the results
if bmi < 18.5:
    print("You are underweight, run to a restaurant while eating chocolate.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight, what about some veggies instead of the deep fried junk food.")
elif bmi >= 30.0:
    print("You are obese, consider moving more and eating less.")