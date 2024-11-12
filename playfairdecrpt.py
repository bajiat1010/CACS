def generate_key_matrix(key):
    key = ''.join(sorted(set(key.lower().replace('j', 'i')), key=lambda x: key.index(x))) + 'abcdefghiklmnopqrstuvwxyz'
    key = ''.join(sorted(set(key), key=key.index))[:25]
    return [key[i:i+5] for i in range(0, len(key), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def preprocess_text(text):
    text = text.lower().replace('j', 'i')
    text = ''.join([char for char in text if char.isalpha()])
    if len(text) % 2 != 0: text += 'x'
    return [text[i:i+2] for i in range(0, len(text), 2)]

def decrypt_digraph(digraph, matrix):
    r1, c1 = find_position(matrix, digraph[0])
    r2, c2 = find_position(matrix, digraph[1])
    if r1 == r2: return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    if c1 == c2: return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    digraphs = preprocess_text(ciphertext)
    return ''.join([decrypt_digraph(d, matrix) for d in digraphs])

# Example usage
key = input("Enter keyword: ")
ciphertext = input("Enter ciphertext: ")
decrypted_text = playfair_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_text)

# Enter keyword: playfair
# Enter plaintext: pranto
# Ciphertext Message: lipqnq
