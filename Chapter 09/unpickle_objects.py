# This program demonstrates object unpickling.
import pickle

# main function
def main():
    end_of_file = False  # To indicate end of file

    # Open a file for binary reading.
    input_file = open('info.dat', 'rb')

    # Read to the end of the file.
    while not end_of_file:
        try:
            # Unpickle the next object.
            person = pickle.load(input_file)

            # Display the object.
            display_data(person)
        except EOFError:
            # Set the flag to indicate the end
            # of the file has been reached.
            end_of_file = True

    # Close the file.
    input_file.close()

# The display_data function displays the person data
# in the dictionary that is passed as an argument.
def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:', person['weight'])
    print()

# Call the main function.
main()
      
