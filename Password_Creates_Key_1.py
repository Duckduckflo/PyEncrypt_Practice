import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password123" 
password = password_provided.encode()

salt = b"\xab\x13\x8a\xe5'f\x1c\xf6\xe6\x97|3\xa3E\xad\xb5"
kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
key = base64.urlsafe_b64encode(kdf.derive(password))
print (key)   
