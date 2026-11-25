"""Assignment 1 - Question 17: Convert distance from kilometres to metres and centimetres."""

kilometres = float(input("Enter distance in kilometres: "))

if kilometres < 0:
    print("Distance cannot be negative.")
else:
    metres = kilometres * 1000
    centimetres = kilometres * 100000
    print(f"{kilometres} km = {metres} metres")
    print(f"{kilometres} km = {centimetres} centimetres")
