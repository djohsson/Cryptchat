#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from crypto.diffiehellman import DiffieHellman
from crypto.aes import AESCipher


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "server":
        port = sys.argv[2]
    elif len(sys.argv) == 3:
        server = True
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        sys.exit("Server usage: python3 main.py 'server' port\
        \nClient usage: python3 main.py address port")

    alice = DiffieHellman()
    bob = DiffieHellman()

    a = alice.gensessionkey(bob.publickey)
    b = bob.gensessionkey(alice.publickey)

    test = AESCipher(a)
    m = "åäö"
    c = test.encrypt(m)
    m2 = test.decrypt(c)
    print("Plaintext: " + m)
    print("Encrypted: " + c)
    print("Decrypted: " + m2)

if __name__ == "__main__":
    main()
