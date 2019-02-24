# Write a definition for a class Book. The Book class has data attributes
# for a title, an author name and the number of pages. The class also has
# the following methods:

# a. An _ _init_ _ method for the class. The method should accept
# arguments for each of the data attributes.

# b. A special _ _len_ _ method to return the number of pages in the book.

# c. An _ _str_ _ method that returns a string showing the state of the
# object

class Book:
    def __init__(self,title,author,pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    
    def __len__(self):
        return int(self.__pages)
    
    def __str__(self):
        return "Title: " + self.__title + \
               "\nAuthor: " + self.__author + \
               "\nPages: " + self.__pages
    