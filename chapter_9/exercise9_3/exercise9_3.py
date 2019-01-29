def encryption_rules():
    encryption_dataset = dict()
    decryption_dataset = dict()
    characters = "!@#$%^&*()_+~`1234567890-={[}]:;>.<,?/AaBbCcFfRrDdTtGgYyHhJjUuKkOoLlp"
    letters = """AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890’'"-.,"""
    for index in range(len(letters)):
        encryption_dataset[letters[index]] = characters[index]
        decryption_dataset[characters[index]] = letters[index]
    return encryption_dataset, decryption_dataset

def main():
    encryption_dataset, decryption_dataset = encryption_rules()
    filename = input('Select a txt file: ')
    print()
    choice = int(input('Press 1 to Encrypt, 2 to Decrypt: '))
    if choice == 1:
        encrypt(filename,encryption_dataset)
    elif choice == 2:
        decrypt(filename,decryption_dataset)
    else:
        print('Not a valid choice')

def encrypt(a_file,encryption_rule):
    # Open the infile and outfile.
    infile = open(a_file,'r', encoding='utf8')
    outfile = open('encrypted_' + a_file,'w', encoding='utf8')
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
            encrypted_line += str(encryption_rule.get(char))
        encrypted_text.append(encrypted_line)
    for line in encrypted_text:
        outfile.write(line + '\n')
    infile.close()
    outfile.close()

def decrypt(a_file,decryption_rules):
    # Open the infile and outfile
    infile = open('encrypted_' + a_file,'r', encoding='utf8')
    outfile = open('decrypted_' + a_file,'w', encoding='utf8')
    # Strip the contents of \n
    encrypted_text = []
    decrypted_text = []
    for line in infile:
        encrypted_text.append(line.rstrip('\n'))
    # For every line in the text file.
    for line in encrypted_text:
        decrypted_line = ''
        # For every character in each line.
        for char in line:
            # Find the character's value in the dictionary
            # and add it to the decrypted text line
            decrypted_line += str(decryption_rules.get(char))
        decrypted_text.append(decrypted_line)
    for line in decrypted_text:
        outfile.write(line + '\n')
    infile.close()
    outfile.close()
main()
