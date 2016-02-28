#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from crypto.diffiehellman import DiffieHellman
from crypto.aes import AESCipher
from network.networkhandler import NetworkHandler
import network.client as client


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "server":
        address = "localhost"
        servermode = True
        port = int(sys.argv[2])
        if len(sys.argv) == 4:
            dhgroup = int(sys.argv[3])
    elif len(sys.argv) >= 3:
        servermode = False
        address = sys.argv[1]
        port = int(sys.argv[2])
        if len(sys.argv) == 4:
            dhgroup = int(sys.argv[3])
    else:
        sys.exit("Server usage: python3 main.py 'server' port [dhgroup]\
        \nClient usage: python3 main.py address port [dhgroup]")

    alice = DiffieHellman()
    bob = DiffieHellman()
    a = alice.gensessionkey(bob.publickey)
    b = bob.gensessionkey(alice.publickey)

    aes1 = AESCipher(a)
    aes2 = AESCipher(b)

    server = NetworkHandler("localhost", 8089, True, alice, aes1)
    client = NetworkHandler("localhost", 8089, False, bob, aes2)
    server.start()
    client.start()

    m = "Secret stuff do not read"
    client.send(m)
    m2 = server.getinmessage()
    print("Decrypted: " + m2)

    client.stop()
    server.stop()


if __name__ == "__main__":
    main()
