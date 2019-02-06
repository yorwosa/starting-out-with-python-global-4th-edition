# This program demonstrates object pickling.
import pickle

# main function
def main():
    again = 'y'  # To control loop repetition
    
    # Open a file for binary writing.
    output_file = open('info.dat', 'wb')

    # Get data until the user wants to stop.
    while again.lower() == 'y':
        # Get data about a person and save it.
        save_data(output_file)

        # Does the user want to enter more data?
        again = input('Enter more data? (y/n): ')

    # Close the file.
    output_file.close()

# The save_data function gets data about a person,
# stores it in a dictionary, and then pickles the
# dictionary to the specified file.
def save_data(file):
    # Create an empty dictionary.
    person = {}
    
    # Get data for a person and store
    # it in the dictionary.
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    # Pickle the dictionary.
    pickle.dump(person, file)

# Call the main function.
main()
