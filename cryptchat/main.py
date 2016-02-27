#/usr/bin/python3
# -*- coding: utf-8 -*-

from crypto.diffiehellman import DiffieHellman
from crypto.aes import AESCipher


def main():
    alice = DiffieHellman()
    bob = DiffieHellman()

    a = alice.gensessionkey(bob.publickey)
    b = bob.gensessionkey(alice.publickey)

    test = AESCipher(a)
    m = u"This is a private message please do not read 「秘密です」"
    m = m.encode('utf8')
    c = test.encrypt(m)
    m2 = test.decrypt(c)
    print("Plaintext: " + m)
    print("Encrypted: " + c)
    print("Decrypted: " + m2)

if __name__ == "__main__":
    main()
