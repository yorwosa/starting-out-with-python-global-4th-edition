def encryption_rules():
    encryption_dataset = dict()
    characters = "~`!@#$%^&*()_+-={[}]:;'?/>.<,1234567890abcdefghijklmnopqrstuvwxABCDE"
    letters = '''AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890'"-.,'''
    for index in range(len(letters)):
        encryption_dataset[letters[index]] = characters[index]
    return encryption_dataset


def main():
    dataset = encryption_rules()
    filename = input('Select a txt file: ')
    print()
    choice = int(input('Press 1 to Encrypt, 2 to Decrypt: '))
    if choice == 1:
        encrypt(filename,dataset)
    elif choice == 2:
        decrypt(filename,dataset)
    else:
        print('Not a valid choice')

def encrypt(a_file,encryption_rules):
    # Open the infile and outfile.
    infile = open(a_file,'r')
    outfile = open('Encrypted_' + a_file,'w')
    # Strip the contents of '\n'
    text = []
    encrypted_text = []
    for line in infile:
        text.append(line.rstrip('\n'))
    # For every line in the text file
    for line in text:
        encrypted_line = ''
        # For every character in each line.
        for char in line:
            # Find the character's value in the dictionary
            # and added to the encrypted text line.
            encrypted_line += str(encryption_rules.get(char))
        encrypted_text.append(encrypted_line)

def decrypt(a_file,decryption_rules):
    
   
   

main()
