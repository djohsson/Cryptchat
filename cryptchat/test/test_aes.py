#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Run from Cryptchat
# python3 -m unittest discover

import unittest
from ..crypto.aes import AESCipher


class testAESCipher(unittest.TestCase):

    def test_encrypt_decrypt(self):
        key = "TTTcPolAhIqZZJY0IOH7Orecb/EEaUx8/u/pQlCgma8="
        cipher = AESCipher(key)
        m = "[TOP SECRET] I like k-pop"
        c = cipher.encrypt(m)
        m2 = cipher.decrypt(c)
        self.assertEqual(m, m2)

    def test_encrypt_decrypt_long(self):
        key = "TTTcPolAhIqZZJY0IOH7Orecb/EEaUx8/u/pQlCgma8="
        cipher = AESCipher(key)
        m = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        c = cipher.encrypt(m)
        m2 = cipher.decrypt(c)
        self.assertEqual(m, m2)

    def test_encrypt_decrypt_unicode(self):
        key = "TTTcPolAhIqZZJY0IOH7Orecb/EEaUx8/u/pQlCgma8="
        cipher = AESCipher(key)
        m = "『秘密』K-popは好きです"
        c = cipher.encrypt(m)
        m2 = cipher.decrypt(c)
        self.assertEqual(m, m2)

    def test_encrypt_decrypt_128(self):
        key = "Ya/C/EvmwW1xWhjM1BgZ/g=="
        cipher = AESCipher(key)
        m = "Private stuff"
        c = cipher.encrypt(m)
        m2 = cipher.decrypt(c)
        self.assertEqual(m, m2)

    def test_encrypt_decrypt_unicode_128(self):
        key = "Ya/C/EvmwW1xWhjM1BgZ/g=="
        cipher = AESCipher(key)
        m = "『秘密』K-popは好きです"
        c = cipher.encrypt(m)
        m2 = cipher.decrypt(c)
        self.assertEqual(m, m2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
