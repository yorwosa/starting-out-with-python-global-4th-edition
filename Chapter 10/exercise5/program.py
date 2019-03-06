# 5. RetailItem Class
# Write a class named RetailItem that holds data about an item in a retail store.
# The class should store the following data in attributes: item description,
# units in inventory, and price.
# Once you have written the class, write a program that creates three RetailItem
# objects and stores the following data in them:

# Description Units in Inventory Price
# Item #1 Jacket 12 59.95
# Item #2 Designer Jeans 40 34.95
# Item #3 Shirt 20 24.95

import retailitem

item1 = retailitem.RetailItem('Jacket',12,59.95)
item2 = retailitem.RetailItem('Designer Jeans',40,34.95)
item3 = retailitem.RetailItem('Shirt',20,24.95)