
def veg_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    j = 0

    for char in plaintext:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')

            p = ord(char) - base
            k = ord(key[j % len(key)].upper()) - ord('A')

            c = (p + k) % 26
            ciphertext += chr(c + base)

            j += 1
        else:
            ciphertext += char

    return ciphertext
