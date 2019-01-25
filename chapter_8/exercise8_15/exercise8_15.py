# Caesar Cipher

# A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a
# letter a certain number of spaces up the alphabet. For example, if shifting the message by
# 13 an A would become an N, while an S would wrap around to the start of the alphabet to
# become an F.
# Write a program that asks the user for a message (a string) and a shift amount (an integer).
# The values should be passed to a function that accepts a string and an integer as arguments,
# and returns a string representing the original string encrypted by shifting the letters by the
# integer. For example, a string of “BEWARE THE IDES OF MARCH” and an integer of 13
# should result in a string of “ORJNER GUR VQRF BS ZNEPU”.

def caesar_cipher(string,integer):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_message = ''
    # for every letter in the string
    for index in range(len(string)):
        # find the position of the letter in alphabet
        original_position = alphabet.find(string[index].upper())
        cipher_position = original_position + integer
        if original_position == -1:
            cipher_message += ' '
        elif cipher_position > len(alphabet):
            cipher_position = cipher_position - 26
            cipher_message += (alphabet[cipher_position])
        else:
            cipher_message += (alphabet[cipher_position])
    return cipher_message


def main():
    message = input('Enter a message: ')
    shift_amount = int(input('Enter a shift amount:'))
    message = caesar_cipher(message,shift_amount)
    print(message)

main()
