def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
def main():
    text = input("Enter the plaintext message: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = encrypt(text, shift)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()


# Enter the plaintext message: pranto
# Enter the shift value: 3
# Encrypted Text: sudqwr
# Decrypted Text: pranto
