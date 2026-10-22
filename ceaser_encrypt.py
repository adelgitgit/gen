
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char
    return result
