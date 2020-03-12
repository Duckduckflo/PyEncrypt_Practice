from cryptography.fernet import Fernet

file = open('key.txt' , 'rb')
key = file.read()
file.close()

message = "my secret message"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print (encrypted)

f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)

original_message = decrypted.decode()
print (original_messge)
