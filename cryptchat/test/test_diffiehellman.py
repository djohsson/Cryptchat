#/usr/bin/python3
# -*- coding: utf-8 -*-
# Run from Cryptchat
# python3 -m cryptchat.test.test_diffiehellman

import unittest
from ..crypto.diffiehellman import DiffieHellman


class testDiffieHellman(unittest.TestCase):

    def test_initiatevalid(self):
        alice = DiffieHellman(group=5)
        self.assertTrue(alice.keysize == 240)

        alice = DiffieHellman(group=17)
        self.assertTrue(alice.keysize == 540)

        alice = DiffieHellman(group=18)
        self.assertTrue(alice.keysize == 620)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
