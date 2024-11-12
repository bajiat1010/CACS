import numpy as np

def mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det = det % mod
    if np.gcd(det, mod) != 1:
        raise ValueError("The key matrix is not invertible under modulo 26.")
    det_inv = pow(det, -1, mod)
    matrix_inv = det_inv * np.round(np.linalg.inv(matrix) * det) % mod
    return matrix_inv.astype(int)

def hill_encrypt(plaintext, key_matrix):
    mod = 26
    plaintext = [ord(char) - 97 for char in plaintext.lower() if char.isalpha()]
    while len(plaintext) % len(key_matrix) != 0:
        plaintext.append(0)
    
    ciphertext = []
    for i in range(0, len(plaintext), len(key_matrix)):
        block = np.array(plaintext[i:i+len(key_matrix)])
        encrypted_block = np.dot(key_matrix, block) % mod
        ciphertext.extend(encrypted_block)
    
    ciphertext = ''.join(chr(i + 97) for i in ciphertext)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    mod = 26
    inverse_key_matrix = mod_inverse(key_matrix, mod)
    
    ciphertext = [ord(char) - 97 for char in ciphertext.lower() if char.isalpha()]
    
    plaintext = []
    for i in range(0, len(ciphertext), len(key_matrix)):
        block = np.array(ciphertext[i:i+len(key_matrix)])
        decrypted_block = np.dot(inverse_key_matrix, block) % mod
        plaintext.extend(decrypted_block)
    
    plaintext = ''.join(chr(i + 97) for i in plaintext)
    return plaintext

def take_matrix_input(n):
    matrix = []
    print(f"Enter the {n}x{n} key matrix:")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    n = int(input("Enter the size of the key matrix (e.g., 2 for 2x2): "))
    key_matrix = take_matrix_input(n)
    
    try:
        plaintext = input("Enter plaintext: ")

        print("\nEncrypted Message: ")
        encrypted_text = hill_encrypt(plaintext, key_matrix)
        print(encrypted_text)
        
        print("\nDecrypted Message: ")
        decrypted_text = hill_decrypt(encrypted_text, key_matrix)
        print(decrypted_text)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# Enter the size of the key matrix (e.g., 2 for 2x2): 2
# Enter the 2x2 key matrix:
# Enter row 1 (space-separated values): 3 3
# Enter row 2 (space-separated values): 2 5
# Enter plaintext: pranto

# Encrypted Message: 
# slnnve

# Decrypted Message: 
# pranto
