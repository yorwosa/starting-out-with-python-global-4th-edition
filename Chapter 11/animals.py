# The Mammal class represents a generic mammal.

class Mammal:

    # The __init__ method accepts an argument for
    # the mammal's species.
    
    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message
    # indicating the mammal's species.
    
    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    
    def make_sound(self):
        print('Grrrrr')

# The Dog class is a subclass of the Mammal class.

class Dog(Mammal):

    # The __init__ method calls the superclass's
    # __init__ method passing 'Dog' as the species.
    
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # The make_sound method overrides the superclass's
    # make_sound method.
    
    def make_sound(self):
        print('Woof! Woof!')

# The Cat class is a subclass of the Mammal class.

class Cat(Mammal):

    # The __init__ method calls the superclass's
    # __init__ method passing 'Cat' as the species.

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # The make_sound method overrides the superclass's
    # make_sound method.

    def make_sound(self):
        print('Meow')
