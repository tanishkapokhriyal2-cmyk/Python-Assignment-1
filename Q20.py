"""Assignment 1 - Question 20: Calculate the quotient and remainder of two numbers."""

dividend = int(input("Enter the dividend (integer): "))
divisor = int(input("Enter the divisor (integer): "))

if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")
