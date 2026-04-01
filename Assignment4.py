'''
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''

# Import math library
import math

# Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the distance between the two points

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Output down below
print("Distance between 2 points is: ", distance)