# Write a class named Patient that has attributes for the following data:
#  • First name, middle name, and last name
#  • Address, city, state, and ZIP code
#  • Phone number
#  • Name and phone number of emergency contact
# The Patient class’s _ _ init _ _ method should accept an argument for each
# attribute. The Patient class should also have accessor and mutator methods for
# each attribute.
# Next, write a class named Procedure that represents a medical procedure that
# has been performed on a patient. The Procedure class should have attributes for the following data:
#  • Name of the procedure
#  • Date of the procedure
#  • Name of the practitioner who performed the procedure
#  • Charges for the procedure
# The Procedure class’s _ _ init _ _ method should accept an argument for each
# attribute. The Procedure class should also have accessor and mutator methods for
# each attribute. Next, write a program that creates an instance of the Patient
# class, initialized with sample data. Then, create three instances of the
# Procedure class, initialized with the following data:

# The program should display the patient’s information, information about all
# three of the procedures, and the total charges of the three procedures.

class Procedure:
    def __init__(self,name,date,practitioner,charge):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
    
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_charge(self):
        return self.__charge
    
    def set_name(self,name):
        self.__name = name
    def set_date(self,date):
        self.__date = date
    def set_practitioner(self,practitioner):
        self.__practitioner = practitioner
    def set_charge(self,charge):
        self.__charge = charge
        
    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nDate: ' + self.__date + \
               '\nPractitioner: ' + self.__practitioner + \
               '\nCharge: ' + self.__charge