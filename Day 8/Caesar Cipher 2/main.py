alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) # To make sure we are always within index range
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#     for letter in cipher_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         original_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {original_text}")

def caesar(direction, text, shift):
    output_text = ''
    multiplier = 1 if direction == 'encode' else -1
    for char in text:
        shifted_position = alphabet.index(char) + (shift * multiplier)
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {direction}d result: {output_text}")

# encrypt(original_text=text, shift_amount=shift)
# decrypt(text, shift)
caesar(direction=direction, text=text, shift=shift)

