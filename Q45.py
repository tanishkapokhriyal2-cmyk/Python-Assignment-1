"""Assignment 1 - Question 45: Accept the length and breadth of a rectangle and display its area."""

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length < 0 or breadth < 0:
    print("Length and breadth cannot be negative.")
else:
    area = length * breadth
    print(f"Area of the rectangle: {area:.2f}")
