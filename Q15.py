"""Assignment 1 - Question 15: Calculate the total and average of five subject marks."""

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print(f"Total Marks: {total:.2f}")
print(f"Average Marks: {average:.2f}")
