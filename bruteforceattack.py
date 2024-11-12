import string

def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_attack(ciphertext):
    print("\nBrute Force Decryption Attempts:")
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

def main():
    plaintext = input("Enter the plaintext message: ")
    shift = int(input("Enter the shift (key) for encryption: "))
    encrypted_text = caesar_encrypt(plaintext, shift)
    print("\nEncrypted Message:", encrypted_text)
    brute_force_attack(encrypted_text)

if __name__ == "__main__":
    main()


# Enter the plaintext message: pranto
# Enter the shift (key) for encryption: 5

# Encrypted Message: uwfsyt

# Brute Force Decryption Attempts:
# Shift 0: uwfsyt
# Shift 1: tverxs
# Shift 2: sudqwr
# Shift 3: rtcpvq
# Shift 4: qsboup
# Shift 5: pranto
# Shift 6: oqzmsn
#...........
