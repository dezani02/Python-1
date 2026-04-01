'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

# Prompt user to enter length and width of rectangle

length = int(input("Enter the Length of the Rectangle: "))
width = int(input("Enter the Width of the Rectangle: "))

# Calculate area of the rectangle

area = length * width

print("Display the calculated area of the rectangle: ", area)