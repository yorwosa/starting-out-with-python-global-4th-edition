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

class RetailItem:
    def __init__(self,description,units,price):
        self.__description = description
        self.__units = units
        self.__price = price
    
    def get_description(self):
        return self.__description
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    
    def set_descripition(self,description):
        self.__description = description
    
    def set_units(self,units):
        self.__units == units
    
    def set_price(self,price):
        self.__price = price