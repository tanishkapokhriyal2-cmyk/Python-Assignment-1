"""Assignment 1 - Question 48: Demonstrate the use of print() with multiple variables and formatted output."""

item = "Laptop"
quantity = 2
unit_price = 54999.50
total_cost = quantity * unit_price

print("Item:", item, "| Quantity:", quantity, "| Unit Price:", unit_price)
print(f"Total cost for {quantity} {item}(s): {total_cost:.2f}")
