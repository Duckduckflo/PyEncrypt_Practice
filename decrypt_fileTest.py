from cryptography.fernet import Fernet

file = open('key.txt' , 'rb')
key = file.read()
file.close()

with open ('Test_secret.txt.encrypted' , 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open('Test_secret.txt.decrypted' , 'wb') as f:
    f.write(encrypted)
