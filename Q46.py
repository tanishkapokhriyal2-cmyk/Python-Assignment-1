"""Assignment 1 - Question 46: Accept five subject marks from the user and display their total."""

total_marks = 0.0
for index in range(1, 6):
    mark = float(input(f"Enter marks for subject {index}: "))
    total_marks += mark

print(f"Total marks across 5 subjects: {total_marks:.2f}")
