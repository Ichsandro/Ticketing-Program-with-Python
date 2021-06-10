# NIM/Nama  : 16519222/Dhimas Adi Nur Fauzi
# Deskripsi :
# B01 - Penyimpanan password berfungsi untuk hashing password user
# Kamus
# Password = String

import hashlib, binascii, os

Password = input("Masukkan password Anda: ")
def hash_password(Password):
    # melakukan hash pada passwword untuk disimpan
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    passwordhash = hashlib.pbkdf2_hmac('sha512', Password.encode('utf-8'), salt, 100000)
    passwordhash = binascii.hexlify(passwordhash)
    return (salt + passwordhash).decode('ascii')

stored_password = hash_password(Password)
print("Password terenkripsi Anda: ", stored_password)
