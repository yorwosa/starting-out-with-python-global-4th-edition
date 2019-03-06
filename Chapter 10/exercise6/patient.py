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

class Paient:
    def __init__(self,first_name,middle_name,last_name,address,city,state,zip_code,
                 phone_number,emergency_contact_name,emergency_contact_number):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_number = emergency_contact_number
    
    def get_first_name(self):
        return self.__first_name
    def get_middle_name(self):
        return self.__middle_name
    def get_last_name(self):
        return self.__last_name
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zip_code(self):
        return self.__zip_code
    def get_phone_number(self):
        return self.__phone_number
    def get_emergency_contact_name(self):
        return self.__emergency_contact_name
    def get_emergency_contact_number(self):
        return self.__emergency_contact_number
    
    def set_first_name(self,first_name):
        self.__first_name = first_name
    def set_middle_name(self,middle_name):
        self.__middle_name = middle_name
    def set_last_name(self,last_name):
        self.__last_name = last_name
    def set_address(self,address):
        self.__address = address
    def set_city(self,city):
        self.__city = city
    def set_state(self,state):
        self.__state = state
    def set_zip_code(self,zip_code):
        self.__zip_code = zip_code
    def set_phone_number(self,phone_number):
        self.__phone_number = phone_number
    def set_emergency_contact_name(self,emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name
    def set_emergency_contact_number(self,emergency_contact_number):
        self.__emergency_contact_number = emergency_contact_number