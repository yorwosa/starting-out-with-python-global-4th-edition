# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped.

def main():
    # Get the test scores from the user.
    scores = get_scores()

    # Get the total of the test scores.
    total = get_total(scores)

    # Get the lowest test score.
    lowest = min(scores)

    # Subtract the lowest score from the total.
    total -= lowest

    # Calculate the average. Note that we divide
    # by 1 less than the number of scores because
    # the lowest score was dropped.
    average = total / (len(scores) - 1)

    # Display the average.
    print('The average, with the lowest score dropped', \
          'is:', average)

# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list is returned.
def get_scores():
    # Create an empty list.
    test_scores = []
    
    # Create a variable to control the loop.
    again = 'y'

    # Get the scores from the user and add them to
    # the list.
    while again == 'y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()
        
    # Return the list.
    return test_scores

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0
    
    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

# Call the main function.
main()
