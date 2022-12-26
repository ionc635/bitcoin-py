import hashlib

def hash256(s):
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

BASE58_ALPHABET = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZAabcdefghijkmnopqrstuvwxyz'

def encode_base58(s):
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    num = int.from_bytes(s, 'big')
    prefix = '1' * count
    result = ''
    while num > 0:
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result

def encode_base58_checksum(b):
    return encode_base58(b + hash256(b)[:4])

def hash160(s):
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()