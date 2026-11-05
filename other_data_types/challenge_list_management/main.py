# initializin lists
meat=["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Main list
deli_dept = [meat, cheese, condiment]
# print the initial state of the list
print("Initial Deli List:", deli_dept)
# Restock Ham
if "Ham" in meat and meat[2]<100:
    meat[2]=100
# New item
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
# Adding the new item to the list
deli_dept.append(seasonal_meat)
# Remove condiment from the list
deli_dept.remove(condiment)
# Sort list
deli_dept.sort()
# print updated list
print("Updated Deli List:", deli_dept)
