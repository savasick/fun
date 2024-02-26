import base64
import hashlib
from cryptography.fernet import Fernet
import os

def string_to_32_byte_key(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.digest()

def encode_key(key):
    return base64.urlsafe_b64encode(key)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def decrypt_folder(path_to_folder, key):
    key = key
    for filename in os.listdir(path_to_folder):
        if os.path.isfile(os.path.join(path_to_folder, filename)):
            decrypt_file(os.path.join(path_to_folder, filename), key)

#passphrase = str('occulta ab occultis')
passphrase = input("Enter passphrase : ")
folder_path = input("Enter path to folder : ")
#folder_path = './test'
passphrase = encode_key(string_to_32_byte_key(passphrase))

try:
    decrypt_folder(folder_path, passphrase)
except:
    print("Error: The passphrase is incorrect.")
