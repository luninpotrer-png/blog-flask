import hashlib

def hashear(password):
    return hashlib.sha256(password.encode()).hexdigest()