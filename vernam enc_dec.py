
def char_to_num(c):
    """Convert a character to its corresponding numerical value (A=0, B=1, ..., Z=25)."""
    return ord(c) - ord('A')

def num_to_char(n):
    """Convert a numerical value back to its corresponding character."""
    return chr(n + ord('A'))

def encrypt(plaintext, key):
    """Encrypt plaintext using the Vernam cipher."""
    ciphertext = []
    
    for p, k in zip(plaintext, key):
        # Convert characters to numbers
        p_num = char_to_num(p)
        k_num = char_to_num(k)
        
        # Apply the XOR operation and wrap around using modulo 26
        encrypted_num = (p_num + k_num) % 26
        
        # Convert back to character
        ciphertext.append(num_to_char(encrypted_num))
    
    return ''.join(ciphertext)

if __name__ == "__main__":
    # Accept plaintext input from the user
    plaintext = input("Enter the plaintext (only uppercase letters): ").upper()
    
    # Accept key input from the user
    key = input("Enter the key (must be the same length as plaintext): ").upper()

    # Check if the key length matches the plaintext length
    if len(key) != len(plaintext):
        print("Error: The key must be of the same length as the plaintext.")
    else:
        # Encrypt the plaintext
        ciphertext = encrypt(plaintext, key)
        print(f"Ciphertext: {ciphertext}")

# -------------------------------------------------------------------------------------------------

def char_to_num(c):
    """Convert a character to its corresponding numerical value (A=0, B=1, ..., Z=25)."""
    return ord(c) - ord('A')

def num_to_char(n):
    """Convert a numerical value back to its corresponding character."""
    return chr(n + ord('A'))

def decrypt(ciphertext, key):
    """Decrypt ciphertext using the Vernam cipher."""
    decrypted_text = []
    
    for c, k in zip(ciphertext, key):
        # Convert characters to numbers
        c_num = char_to_num(c)
        k_num = char_to_num(k)
        
        # Apply the XOR operation and wrap around using modulo 26
        decrypted_num = (c_num - k_num) % 26
        
        # Convert back to character
        decrypted_text.append(num_to_char(decrypted_num))
    
    return ''.join(decrypted_text)

if __name__ == "__main__":
    # Accept ciphertext input from the user
    ciphertext = input("Enter the ciphertext (only uppercase letters): ").upper()
    
    # Accept key input from the user
    key = input("Enter the key (must be the same length as ciphertext): ").upper()

    # Check if the key length matches the ciphertext length
    if len(key) != len(ciphertext):
        print("Error: The key must be of the same length as the ciphertext.")
    else:
        # Decrypt the ciphertext
        decrypted_text = decrypt(ciphertext, key)
        print(f"Decrypted Text: {decrypted_text}")



# Enter the plaintext (only uppercase letters): CRYPTO
# Enter the key (must be the same length as plaintext): PRANTO
# Ciphertext: RIYCMC
# Enter the ciphertext (only uppercase letters): RIYCMC
# Enter the key (must be the same length as ciphertext): PRANTO
# Decrypted Text: CRYPTO