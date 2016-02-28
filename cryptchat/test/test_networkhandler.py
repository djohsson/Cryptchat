#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Run from Cryptchat
# python3 -m unittest discover

import unittest
from ..network.networkhandler import NetworkHandler
from ..crypto.aes import AESCipher
from ..crypto.diffiehellman import DiffieHellman


class testNetworkHandler(unittest.TestCase):

    def setUp(self):
        alice = DiffieHellman()
        bob = DiffieHellman()
        a = alice.gensessionkey(bob.publickey)
        b = bob.gensessionkey(alice.publickey)

        aes1 = AESCipher(a)
        aes2 = AESCipher(b)

        self.server = NetworkHandler("localhost", 8090, True, alice, aes1)
        self.client = NetworkHandler("localhost", 8090, False, bob, aes2)


    def test_sendmessage(self):
        self.server.start()
        self.client.start()

        m = "This is secret please do not read. And some chars to get unicode-testing out of the way åäö"
        self.client.send(m)
        m2 = self.server.getinmessage()
        self.assertEqual(m, m2)


    def tearDown(self):
        self.server.stop()
        self.client.stop()

def main():
    unittest.main()

if __name__ == '__main__':
    main()
