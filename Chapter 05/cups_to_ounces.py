# This program converts cups to fluid ounces.

def main():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups: '))
    # Convert the cups to ounces.
    cups_to_ounces(cups_needed)

# The intro function displays an introductory screen.
def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is:')
    print('    1 cup = 8 fluid ounces')
    print()

# The cups_to_ounces function accepts a number of
# cups and displays the equivalent number of ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, 'ounces.')

# Call the main function.
main()
