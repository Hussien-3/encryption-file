from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter


# key = Random.new().read(16) // b'\xaf\x8e\xb4\x92\xcd\xd9\x05\x9c\xf3V\xcc\x93\x98\x97\xe2\x92'


def encryption(key, fullpath):
    counter = Counter.new(128)
    c = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, "r+b") as f:
        plaintext = f.read(16)
        while plaintext:
            f.seek(-len(plaintext), 1)
            f.write(c.encrypt(plaintext))
            plaintext = f.read(16)


def decryption(key, fullpath):
    counter = Counter.new(128)
    c = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, "r+b") as f:
        plaintext = f.read(16)
        while plaintext:
            f.seek(-len(plaintext), 1)
            f.write(c.decrypt(plaintext))
            plaintext = f.read(16)


fullpath = "write fullpath"
key = "write key use (Random)"


encryption(key, fullpath)
decryption(key, fullpath)
