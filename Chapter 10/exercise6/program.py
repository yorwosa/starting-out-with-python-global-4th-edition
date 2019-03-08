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
# each attribute.

# Next, write a program that creates an instance of the Patient
# class, initialized with sample data.

# Then, create three instances of the
# Procedure class, initialized with the following data:

# The program should display the patient’s information, information about all
# three of the procedures, and the total charges of the three procedures.

import patient
import procedure

def createobjects():
    patient0 = patient.Patient('John','Pika','Doe','Nice street 30',
                               'New York','NY','NY10503',
                               '12341234','Yeadsgfd','13241235')

    procedure1 = procedure.Procedure('Laser αμφιβλιστροϊδή','5/5/1990',
                                     'Dr. Μπαμπης Παπαδημητρίου','30.000 δρχ.')
    procedure2 = procedure.Procedure('Αφαιρεση Χολής', '10/9/2000','Dr Μαρία Τσακαλώτου',
                                     '500 ευρώ')
    procedure3 = procedure.Procedure('Βλαστοκυτταρική αναγέννηση', '23/12/2018',
                                     'Dr Frankenstein', '50.000 ευρώ')
    return(patient0,procedure1,procedure2,procedure3)
def main():
     pat,proc1,proc2,proc3 = createobjects()
     print(pat)
     print()
     print(proc1)
     print()
     print(proc2)
     print()
     print(proc3)

main()