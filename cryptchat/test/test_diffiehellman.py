#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Run from Cryptchat
# python3 -m unittest discover

import unittest
from ..crypto.diffiehellman import DiffieHellman


class testDiffieHellman(unittest.TestCase):

    def test_privatekeysize(self):
        testgroups = [5, 14, 16, 17, 18]
        for group in testgroups:
            alice = DiffieHellman(group=group)
            self.assertTrue(alice.privatekey.bit_length() == alice.keysize)

    def test_equalsessionkey(self):
        testgroups = [5, 17]
        for group in testgroups:
            alice = DiffieHellman(group=group)
            bob = DiffieHellman(group=group)
            a = alice.gensessionkey(bob.publickey)
            b = bob.gensessionkey(alice.publickey)
            self.assertEqual(a, b)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
