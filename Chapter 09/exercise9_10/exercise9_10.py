##Write a program that reads the contents of a text file. The program should create a diction-
##ary in which the key-value pairs are described as follows:
##• Key. The keys are the individual words found in the file.
##• Values. Each value is a list that contains the line numbers in the file where the word
##(the key) is found.
##For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary
##would contain an element in which the key was the string “robot”, and the value was a list
##containing the numbers 7, 18, 94, and 138.
##Once the dictionary is built, the program should create another text file, known as a word
##index, listing the contents of the dictionary. The word index file should contain an alpha-
##betical listing of the words that are stored as keys in the dictionary, along with the line
##numbers where the words appear in the original file. Figure 9-1 shows an example of an
##original text file ( Kennedy.txt ) and its index file ( index.txt ).

# Open a text file.
# Read the contents
# Every time a new word appers, create a new key with value a list with a single
# element, which will be the lien where the word appeared.
# Every time a word that already exists appears, add to the list of that key,
# the line that appeared.
# Create another text file
# Sort the keys alphabetically
# Write each word and the times it appeared with a colon (:) in between.

def get_textname():
    # Ask the use the name of the text file to create an index for.
    name = input('For which file would you like me to create a word index? ')
    return name

def create_dictionary(filename):
    infile = open(filename, 'r', encoding='utf8') # Open the file
    word_index = dict() # Create an empty dictionary to store the words and line numbers
    counter = 0 # Set a counter to count the line we found the word
    for line in infile:
        wordlinelist = line.rstrip('\n').split() # remove \n and split the line into words.
        counter += 1 # advance the counter to reflect the line we are in
        for word in wordlinelist: # for every word in the line
            if word not in word_index: # If we haven't yet encountered it,
                word_index[word] = [str(counter)] # Start a key/value pair with value being a list with the line number.
            elif word in word_index: # If the word was found,
                word_index[word].append(str(counter)) # Append the line number to the list in the value
    infile.close() # Close the file since we are done reading.
    return word_index

def create_index_file(dict):
    outfile = open('index.txt', 'w', encoding='utf8') # create a file to store the word index.
    a_list = [] # Create a list to store the word the index.
    index = 0 # Create a counter to control the index we are checking.
    for key in dict.keys(): # Ever word found in the dictionary
        a_list.append(key) # Append it to the a_list
        for value in dict[key]: # Ever value found for that word/key
            a_list[index] = a_list[index] + ' ' + value # Add it to the a_list, in the same index, seperated by a space
        index += 1 # Advance the index by one to continue to the next word.
    a_list.sort() # Sort the finished list.
    for element in a_list:
        outfile.write(element + '\n') # Extract the list, element by element to the file index.txt.
    outfile.close() # Close the file
             
            
def main():
    print('This program creates a word index of the file you request.')
    print('----------------------------------------------------------')
    print()
    file = get_textname() # Ask the user for the file to create an index for.
    dictionary = create_dictionary(file) # Create the dictionary for the file.
    create_index_file(dictionary) # Write the the word index to a file.
    print('Word index is created. File name is: index.txt')

# Call the main function.
main()