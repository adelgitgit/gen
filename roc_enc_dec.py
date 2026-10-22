
def rot13_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.islower():
            # Find the position of the character in the alphabet
            position = ord(char) - ord('a')
            # Encrypt the character by shifting it 13 places
            encrypted_char = chr((position + 13) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            # If the character is not a lowercase letter, leave it as is
            encrypted_text += char
    return encrypted_text
