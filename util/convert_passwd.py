import uuid
import hashlib

def convert(passwd, salt = None):
    if salt is None:
        salt = uuid.uuid4().hex
        hashed_passwd = hashlib.sha256(passwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return salt, hashed_passwd
    else:
        hashed_passwd = hashlib.sha256(passwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return hashed_passwd