from cryptography.fernet import Fernet

file = open ('key.txt' , 'rb')
key = file.read()
file.close()
print (key)
