"""Assignment 1 - Question 5: Demonstrate valid and invalid Python identifiers."""

import keyword

# Valid Python identifiers (start with letter or underscore, contain letters, digits, underscores)
student_name = "Riya"
_roll_no = 101
marks2 = 95
TotalScore = 480

print("Valid identifiers and their values:")
print("student_name =", student_name)
print("_roll_no =", _roll_no)
print("marks2 =", marks2)
print("TotalScore =", TotalScore)

# Examples of invalid identifiers (commented out so the script runs without SyntaxError):
# 2marks = 80       # Invalid: starts with a digit
# student-name = 1  # Invalid: contains a hyphen (-)
# my var = 10       # Invalid: contains a space
# class = "CS"      # Invalid: 'class' is a reserved keyword

candidates = ["student_name", "_roll_no", "marks2", "2marks", "student-name", "my var", "class"]
print("\nChecking identifier validity:")
for name in candidates:
    is_valid = name.isidentifier() and not keyword.iskeyword(name)
    status = "Valid" if is_valid else "Invalid"
    print(f"  {name!r}: {status}")
