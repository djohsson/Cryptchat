#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Run from Cryptchat
# python3 -m unittest discover

import unittest
from ..network.networkhandler import NetworkHandler
from ..crypto.diffiehellman import DiffieHellman


class testNetworkHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        alice = DiffieHellman()
        bob = DiffieHellman()
        a = alice.gensessionkey(bob.publickey)
        b = bob.gensessionkey(alice.publickey)

        cls.server = NetworkHandler("localhost", 8090, True, alice)
        cls.client = NetworkHandler("localhost", 8090, False, bob)
        cls.server.start()
        cls.client.start()

    def test_sendmessage(self):
        m = "This is secret please do not read. And some chars to get unicode-testing out of the way åäö"
        self.client.send(m)
        m2 = self.server.receive()
        self.assertEqual(m, m2)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
