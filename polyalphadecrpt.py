def decrypt_polyalphabetic(ciphertext, keyword):
  """Decrypts a ciphertext message using a Vigenère cipher.

  Args:
    ciphertext: The ciphertext message to decrypt.
    keyword: The keyword used for encryption.

  Returns:
    The decrypted plaintext.
  """

  plaintext = ""
  keyword_index = 0

  for char in ciphertext:
    if char.isalpha():
      shift = ord(keyword[keyword_index % len(keyword)].upper()) - ord('A')
      decrypted_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
      plaintext += decrypted_char
      keyword_index += 1
    else:
      plaintext += char

  return plaintext
ciphertext=input("The ciphertext message to decrypt: " )
keyword=input("The keyword used for encryption:" )
plaintext = decrypt_polyalphabetic(ciphertext, keyword)
print("Plaintext:",plaintext)


# Enter the plaintext: pranto
# Enter the keyword:polyalpha
# Ciphertext: EFLLTZ