from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption

import OpenSSL

key = ec.generate_private_key(ec.SECP256R1(), default_backend())
print(key)
key_pem = key.private_bytes(encoding=Encoding.PEM, format=PrivateFormat.TraditionalOpenSSL, encryption_algorithm=NoEncryption())
print(key_pem)
print(OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, key_pem))