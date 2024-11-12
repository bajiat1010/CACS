def encrypt(plaintext, key):
    """Encrypt plaintext using the Vernam cipher."""
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

# def decrypt(ciphertext, key):
#     """Decrypt ciphertext using the Vernam cipher."""
#     decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
#     return decrypted_text

if __name__ == "__main__":
    plaintext = input("Enter the plaintext (only uppercase letters): ").upper()

    key = input("Enter the key (must be the same length as plaintext): ").upper()
    
    if len(key) != len(plaintext):
        print("Error: The key must be of the same length as the plaintext.")
    else:
        ciphertext = encrypt(plaintext, key)
        print(f"Ciphertext: {''.join(format(ord(c), '02x') for c in ciphertext)}")  # Display as hex for readability

        # decrypted_text = decrypt(ciphertext, key)
        # print(f"Decrypted Text: {decrypted_text}")

        

# Enter the plaintext (only uppercase letters): PRANTO
# Enter the key (must be the same length as plaintext): VERNAM
# Ciphertext: 061713001502
