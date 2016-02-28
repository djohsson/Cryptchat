#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base64 import b64encode, b64decode
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher():

    def __init__(self, key):
        self.key = b64decode(key)

    def encrypt(self, m):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return b64encode(iv + cipher.encrypt(m)).decode("utf8")

    def decrypt(self, c):
        c = b64decode(c)
        iv = c[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return cipher.decrypt(c[AES.block_size:]).decode("utf8")
