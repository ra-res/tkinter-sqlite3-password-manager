import bcrypt
import cryptography
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Password():
    def password_encrypt(self, _password):
        temp_pass = _password.encode()
        key = self.generate_key(temp_pass)
        f = Fernet(key)
        encrypted = f.encrypt(temp_pass)
        return encrypted.decode(), key.decode()

    def generate_salt(self):
        return os.urandom(16)   

    def password_decrypt(self, _encrypted_pass, _key):
        f = Fernet(_key)
        decrypted = f.decrypt(_encrypted_pass.encode())
        return decrypted.decode()

    def generate_key(self, _password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.generate_salt(),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(_password))
        return key




# test = Password()
# encr = test.password_encrypt("Rares")
# print(encr[0], encr[1])
# decr=test.password_decrypt(encr[0], encr[1])
# print(decr)