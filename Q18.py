"""Assignment 1 - Question 18: Calculate the volume of a cube and a cuboid."""

side = float(input("Enter the side length of the cube: "))
length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

if side < 0 or length < 0 or breadth < 0 or height < 0:
    print("Dimensions cannot be negative.")
else:
    cube_volume = side ** 3
    cuboid_volume = length * breadth * height
    print(f"Volume of the cube: {cube_volume:.2f}")
    print(f"Volume of the cuboid: {cuboid_volume:.2f}")
