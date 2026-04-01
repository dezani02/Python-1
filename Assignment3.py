'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''

# Prompt user to enter their weight in kilograms and height in meters

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# Calculate the BMI

BMI = weight / (height ** 2)

print("Your BMI is: ", BMI)