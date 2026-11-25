"""Assignment 1 - Question 9: Swap two variables using a temporary variable."""

first_num = input("Enter the first value: ")
second_num = input("Enter the second value: ")

print(f"Before swapping: first_num = {first_num}, second_num = {second_num}")

temp = first_num
first_num = second_num
second_num = temp

print(f"After swapping: first_num = {first_num}, second_num = {second_num}")
