#/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher():

    def __init__(self, key):
        self.key = key
        self.bs = 16

    def encrypt(self, m):
        m = self.pad(m)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(m))

    def decrypt(self, c):
        c = base64.b64decode(c)
        iv = c[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(c[AES.block_size:]))

    def pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
