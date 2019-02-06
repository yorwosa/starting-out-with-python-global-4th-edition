#File Analysis
#
#This program reads the contents of two text files and compares them.
#1. It displays a list of all the unique words contained in both files.
#2. It displays a list of the words that appear in both files.
#3. It displays a list of words that appear in the first file but not the second
#4. It displays a list of words that appear in the 2nd file but not the 1st.
#5. It displays a list of words that appear in either the 1st or 2nd file, but
#not in both

# This function requests the two files for comparison
def comparefiles(file1,file2):    
    print()
    print('All the words that appear in the files.')
    print(file1.union(file2))
    print()
    
    print('Only the words that appear in both files.')
    print()
    print(file1.intersection(file2))
    print()
    
    print('Words that appear in the first but not the second')
    print(file1.difference(file2))
    print()
    
    print('Words that appear in the second but not the first.')
    print(file2.difference(file1))
    print()
    print('Words that appear either in the 1st or 2nd but not in both.')
    print(file1.symmetric_difference(file2))

def getFileNames():
    file1 = input('First file: ')
    file2 = input('Second file: ')
    return file1, file2


def main():
    # Request the files
    file_1, file_2 = getFileNames()
    # Open the files.
    firstFile = open(file_1, 'r')
    secondFile = open(file_2, 'r')
    contents1 = firstFile.read()
    contents2 = secondFile.read()
    contents1 = contents1.split()
    contents2 = contents2.split()
    con1 = set(contents1)
    con2 = set(contents2)
    comparefiles(con1,con2)

main()