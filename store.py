# Variables Section

customer_name = "Alex"
items_purchased = 12
items_price = 20.50
is_member = True

print("CUSTOMER INFORMATION")
print("Customer Name:", customer_name)
print("Items Purchased:", items_purchased)
print("Price per Item:", items_price)
print("Store Member:", is_member)
print()

# Arthemtic Section

print("ARTHMETIC CALCULATIONS")

extra_items = 2
total_items = items_purchased + extra_items
print("Total Items After Adding More:", total_items)

double_items = items_purchased * 2
print("Items Doubled:", double_items)

average_cost = items_price / 2
print("Half Price Example:", average_cost)
print()

# Constants Section

PI = 3.14159
MAX_USERS = 100

print("CONSTANT VALUES")
print("PI:", PI)
print("Maximum Users Allowed:", MAX_USERS)
print()

# meaningful expression section

print("TOTAL PURCHASE CALCULATION")

total_cost = items_purchased * items_price

print("Items Purchased:". items_purchased)
print("Item Price:", items_price)
print("Total Cost:", total_cost)

# Selection Section

# Relational operation
if items_purchased > 10:
    print("Customer bought more than 10 items.")
else:
    print("Customer bought 10 or few items.")

# Logical Operation
if is_member and items_purchased > 5:
    print("Customer qualifies for at least one promotion.")

if items_purchased > 5 or is_member:
    print("Customer qualifies for at least one promotion.")
    
if not is_member:
    print("Customer is not a store member.")

print()
print("Completed.")


