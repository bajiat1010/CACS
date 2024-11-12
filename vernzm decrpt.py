
def decrypt(ciphertext, key):
    """Decrypt ciphertext using the Vernam cipher."""
    decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return decrypted_text

if __name__ == "__main__":
    # Accept ciphertext input from the user
    ciphertext_input = input("Enter the ciphertext (in hexadecimal format): ")
    
    # Convert hex input to string
    ciphertext = ''.join(chr(int(ciphertext_input[i:i+2], 16)) for i in range(0, len(ciphertext_input), 2))

    # Accept key input from the user
    key = input("Enter the key (must be the same length as ciphertext): ")

    # Check if the key length matches the ciphertext length
    if len(key) != len(ciphertext):
        print("Error: The key must be of the same length as the ciphertext.")
    else:
        # Decrypt the ciphertext
        decrypted_text = decrypt(ciphertext, key)
        print(f"Decrypted Text: {decrypted_text}")




# Enter the ciphertext (in hexadecimal format): 061713001502
# Enter the key (must be the same length as ciphertext): VERNAM
# Decrypted Text: PRANTO


