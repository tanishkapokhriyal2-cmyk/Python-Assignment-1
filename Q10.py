"""Assignment 1 - Question 10: Swap two variables without using a temporary variable."""

first_val = input("Enter the first value: ")
second_val = input("Enter the second value: ")

print(f"Before swapping: first_val = {first_val}, second_val = {second_val}")

first_val, second_val = second_val, first_val

print(f"After swapping: first_val = {first_val}, second_val = {second_val}")
