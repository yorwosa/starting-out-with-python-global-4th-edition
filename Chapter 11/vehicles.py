# The Automobile class holds general data
# about an automobile in inventory.

class Automobile:
    # The __init__ method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values.
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # The following methods are mutators for the
    # class's data attributes.
    
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The following methods are the accessors
    # for the class's data attributes.
    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

# The Car class represents a car. It is a subclass
# of the Automobile class.

class Car(Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.
    
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __doors attribute.
        self.__doors = doors

    # The set_doors method is the mutator for the
    # __doors attribute.

    def set_doors(self, doors):
        self.__doors = doors

    # The get_doors method is the accessor for the
    # __doors attribute.

    def get_doors(self):
        return self.__doors

# The Truck class represents a pickup truck. It is a
# subclass of the Automobile class.

class Truck(Automobile):
    # The __init__ method accepts arguments for the
    # truck's make, model, mileage, price, and drive type.
    
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __drive_type attribute.
        self.__drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # __drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # The get_drive_type method is the accessor for the
    # __drive_type attribute.

    def get_drive_type(self):
        return self.__drive_type

# The SUV class represents a sport utility vehicle. It
# is a subclass of the Automobile class.

class SUV(Automobile):
    # The __init__ method caccepts arguments for the
    # SUV's make, model, mileage, price, and passenger
    # capacity.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap

    # The set_pass_cap method is the mutator for the
    # __pass_cap attribute.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the
    # __pass_cap attribute.

    def get_pass_cap(self):
        return self.__pass_cap
