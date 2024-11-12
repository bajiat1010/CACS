import string
import random
def generate_cipher_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet.copy()
    
    random.shuffle(shuffled_alphabet)
    cipher_key = dict(zip(alphabet, shuffled_alphabet))
    return cipher_key
def encrypt(plaintext, cipher_key):
    ciphertext = ""
    for char in plaintext.lower():
        if char in cipher_key:
            ciphertext += cipher_key[char]
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, cipher_key):
    reverse_key = {v: k for k, v in cipher_key.items()}
    plaintext = ""
    for char in ciphertext.lower():
        if char in reverse_key:
            plaintext += reverse_key[char]
        else:
            plaintext += char  
    return plaintext
def main():
    plaintext = input("Enter the plaintext message: ")
    cipher_key = generate_cipher_key()
    encrypted_text = encrypt(plaintext, cipher_key)
    decrypted_text = decrypt(encrypted_text, cipher_key)
    print("Encrypted Message:", encrypted_text)
    print("Decrypted Message:", decrypted_text)

if __name__ == "__main__":
    main()


# Enter the plaintext message: good morning! Pranto.
# Encrypted Message: jxxz wxmutuj! dmruax.
# Decrypted Message: good morning! pranto.
