grocery_items = "milk cheese bread apples oranges chicken"
# Dairy product 1
dairy1 = grocery_items[0:5]
# Dairy product 2
dairy2 = grocery_items[5:11]
# Bakery product 1
bakery1 = grocery_items[12:17]
# Putting those products together 
products_together = dairy1 + ", " + dairy2 + ", " + bakery1
# printing what product we have in aisle 5
message = f"We have daire and bakery items: {products_together} in aisle 5"
print(message)