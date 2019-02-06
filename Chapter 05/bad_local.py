# Definition of the main function.
def main():
    get_name()
    print('Hello', name)     # This causes an error!

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')

# Call the main function.
main()
