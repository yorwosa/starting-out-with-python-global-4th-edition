# This program lists the unique words found in a specified file.
def CountUniqueWords(file):
    # Open with utf8 encoding
    infile = open(file, 'r', encoding='utf8')
    # Create a set to store and pick the unique words.
    uniqueWords = set()
    # Split the text into words
    for line in infile:
        temp_line = line.split()
        for word in temp_line:
            # Strip the test of characters and make every word lowercase.
            word = word.strip('''~`!@# $%^&*()_+=-{}][:;"'<,>.?/''').lower()
            # Add the word to the set
            uniqueWords.add(word)
    # Turn the set into a list.
    uniqueWords = list(uniqueWords)
    # Display the results
    print('These are the unique words found in this file')
    print('---------------------------------------------')
    # Print all the words except the last one in the list
    # with a following comma
    for word in uniqueWords[:-1]:
        print(word + ',',end='')
    # Print the last word.
    print(uniqueWords[-1])

def main():
    print('This program will count the number of unique words in a file.')
    print()
    
    # Get the filname form the user.
    filename = input('Please select a filename: ')
    CountUniqueWords(filename)

# Call the main function.
main()