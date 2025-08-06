import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

key = Random.new().read(16)


def encrypt_file(key, fullpath):
    counter = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, "r+b") as f:
        data = f.read()
        f.seek(0)
        f.write(cipher.encrypt(data))


def decrypt_file(key, fullpath):
    counter = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, "r+b") as f:
        data = f.read()
        f.seek(0)
        f.write(cipher.decrypt(data))


def process_folder(fullpath, key, mode="encrypt"):
    for root, dirs, files in os.walk(fullpath):
        for file in files:
            full_path = os.path.join(root, file)
            if mode == "encrypt":
                encrypt_file(key, full_path)
            elif mode == "decrypt":
                decrypt_file(key, full_path)


key = "write key"
fullpath = "write fullpath"
mode = "encrypt || decrypt"

encrypt_file(key, fullpath)
encrypt_file(key, fullpath)
process_folder(key, fullpath, mode)
