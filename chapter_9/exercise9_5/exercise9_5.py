# This program generates 100 random numbers from 1 to 10.
# Then displays the frequency of the numbers.

import random

def generateNumbers():
    # Create a dictionary
    numberdict = dict()
    # Create random numbers and save them to the dictionary.
    for count in range(100):
        number = random.randint(1,10)
        # If not already in dictonary, add it.
        if number not in numberdict:
            numberdict[number] = 1
        # If already in dictionary , raise the value by 1
        else:
            numberdict[number] += 1
    return numberdict

def main():
    numbers = generateNumbers()
    # print the results.
    for number in range(1,11):
        print(number,'appeared:',numbers[number],'times.')

# Call the main function
main()