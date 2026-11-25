"""Assignment 1 - Question 14: Calculate simple interest using principal, rate and time."""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (%): "))
time = float(input("Enter the time period (in years): "))

if principal < 0 or rate < 0 or time < 0:
    print("Principal, rate, and time cannot be negative.")
else:
    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest: {simple_interest:.2f}")
