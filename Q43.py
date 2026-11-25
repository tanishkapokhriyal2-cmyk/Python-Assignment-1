"""Assignment 1 - Question 43: Accept a student's name using input() and display a welcome message."""

student_name = input("Enter the student's name: ").strip()
if not student_name:
    student_name = "Student"

print(f"Welcome, {student_name}! Wishing you great success in Python programming.")
