def encrypt_polyalphabetic(plaintext, keyword):
  ciphertext = ""
  keyword_index = 0

  for char in plaintext:
    if char.isalpha():
      shift = ord(keyword[keyword_index % len(keyword)].upper()) - ord('A')
      encrypted_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
      ciphertext += encrypted_char
      keyword_index += 1
    else:
      ciphertext += char

  return ciphertext
plaintext=input("Enter the plaintext: " )
keyword=input("Enter the keyword:" )
ciphertext = encrypt_polyalphabetic(plaintext, keyword)
print("Ciphertext:",ciphertext)


# Enter the plaintext: pranto
# Enter the keyword:polyalpha
# Ciphertext: EFLLTZ
