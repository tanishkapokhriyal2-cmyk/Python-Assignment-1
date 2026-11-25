"""Assignment 1 - Question 11: Calculate the area and perimeter of a rectangle."""

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length < 0 or breadth < 0:
    print("Length and breadth cannot be negative.")
else:
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")
