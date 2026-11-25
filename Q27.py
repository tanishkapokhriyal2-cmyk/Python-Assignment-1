"""Assignment 1 - Question 27: Demonstrate the use of int(), float() and str() functions."""

raw_value = "25"
as_int = int(raw_value)
as_float = float(raw_value)
back_to_str = str(as_float)

print("int('25') ->", as_int, "| Type:", type(as_int))
print("float('25') ->", as_float, "| Type:", type(as_float))
print("str(25.0) ->", repr(back_to_str), "| Type:", type(back_to_str))
