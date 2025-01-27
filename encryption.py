import random 
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = list.copy(chars)
random.shuffle(keys)
usr_input = input("Enter your message to encrypt: ")
cipher = ""

# ENCRYPT
for letter in usr_input:
    index = chars.index(letter)
    cipher += keys[index]
print(f"Original message: {usr_input}")
print(f"Encrypted message: {cipher}")

# DECRYPT
plain_txt = input("Enter the message to decrypt: ")
decrypt = ""
for letter in plain_txt:
    index = keys.index(letter)
    decrypt += chars[index]
print(f"Encrypted message: {plain_txt}")
print(f"Decrypted message: {decrypt}")