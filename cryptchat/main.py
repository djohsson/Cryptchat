#/usr/bin/python3
# -*- coding: utf-8 -*-

from crypto.diffiehellman import DiffieHellman


def main():
    print("Hello world")
    alice = DiffieHellman()
    bob = DiffieHellman()

    a = alice.gensessionkey(bob.publickey)
    b = bob.gensessionkey(alice.publickey)

if __name__ == "__main__":
    main()
