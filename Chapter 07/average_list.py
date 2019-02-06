# This program calculates the average of the values
# in a list.

def main():
    # Create a list.
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # Create a variable to use as an accumulator.
    total = 0.0
    
    # Calculate the total of the list elements.
    for value in scores:
        total += value

    # Calculate the average of the elements.
    average = total / len(scores)
    
    # Display the total of the list elements.
    print('The average of the elements is', average)

# Call the main function.
main()
