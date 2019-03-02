# 1. Pet Class
#  Write a class named Pet , which should have the following data attributes:
#    • _ _ name (for the name of a pet)
#    • _ _ animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
#        and ‘Bird’)
#    • _ _ age (for the pet’s age)

# The Pet class should have an _ _ init _ _ method that creates these
# attributes. It should also have the following methods:

#   • set_name
#     This method assigns a value to the _ _ name field.
#   • set_animal_type
#     This method assigns a value to the _ _ animal_type field.
#   • set_age
#     This method assigns a value to the _ _ age field.
#   • get_name
#     This method returns the value of the _ _ name field.
#   • get_animal_type
#     This method returns the value of the _ _ animal_type field.
#   • get_age
#     This method returns the value of the _ _ age field.

#Once you have written the class, write a program that creates an object of the class and
#prompts the user to enter the name, type, and age of his or her pet. This data should be
#stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s
#name, type, and age and display this data on the screen.

import exercise1

name = input('What is the name of your pet? ')
animal_type = input('What kind of animal is it? ')
age = input('How old is it? ')

my_pet = exercise1.Pet(name,animal_type,age)
print('You have a',my_pet.get_animal_type(),'named',my_pet.get_name(),'and it is',my_pet.get_age(),'years old.')