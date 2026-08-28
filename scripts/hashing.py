import hashlib

def hash224(text, salt=None):
    if salt is None: return hashlib.sha224(text.encode()).hexdigest()
    else: return hashlib.sha224((text+salt).encode()).hexdigest()

def hash256(text, salt=None):
    if salt is None: return hashlib.sha256(text.encode()).hexdigest()
    else: return hashlib.sha256((text+salt).encode()).hexdigest()

def hash384(text, salt=None):
    if salt is None: return hashlib.sha384(text.encode()).hexdigest()
    else: return hashlib.sha384((text+salt).encode()).hexdigest()

def hash512(text, salt=None):
    if salt is None: return hashlib.sha512(text.encode()).hexdigest()
    else: return hashlib.sha512((text+salt).encode()).hexdigest()