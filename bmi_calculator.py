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
# formatted float to 2f precision to print double decimal digit 
bmi = kg / (cm / 100)**2
print ("Your BMI index is:  {:.2f}" .format (bmi))

# Bonus code for displaying BMI category based on the results
if bmi < 18.5:
    print("You are underweight, run to a restaurant while eating chocolate.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight, what about some veggies instead of the deep fried junk food.")
elif bmi >= 30.0:
    print("You are obese, consider moving more and eating less.")

# Used references:
# https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/
# https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html
# https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g
# https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place
# https://stackoverflow.com/questions/66451180/i-want-to-know-the-difference-between-0-and-1f-in-format-method