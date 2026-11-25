"""Assignment 1 - Question 13: Calculate the area of a triangle using its base and height."""

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

if base < 0 or height < 0:
    print("Base and height cannot be negative.")
else:
    area = 0.5 * base * height
    print(f"Area of the triangle: {area:.2f}")
