# This program uses recursion to calculate
# the factorial of a number.

def main():
    # Get a number from the user.
    number = int(input('Enter a nonnegative integer: '))

    # Get the factorial of the number.
    fact = factorial(number)

    # Display the factorial.
    print('The factorial of', number, 'is', fact)

# The factorial function uses recursion to
# calculate the factorial of its argument,
# which is assumed to be nonnegative.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Call the main function.
main()
