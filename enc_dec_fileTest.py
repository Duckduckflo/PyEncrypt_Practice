from cryptography.fernet import Fernet

file = open('key.txt' , 'rb')
key = file.read()
file.close()

with open ('Test_secret.txt' , 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('Test_secret.txt.encrypted' , 'wb') as f:
    f.write(encrypted)
