"""Assignment 1 - Question 12: Calculate the area and circumference of a circle."""

PI = 3.14159
radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("Radius cannot be negative.")
else:
    area = PI * radius * radius
    circumference = 2 * PI * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")
