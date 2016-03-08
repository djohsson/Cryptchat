#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from cryptchat.crypto.diffiehellman import DiffieHellman
from cryptchat.crypto.aes import AESCipher
from cryptchat.network.networkhandler import NetworkHandler
from cryptchat.gui.gui import GUI


def main():
    # if len(sys.argv) >= 3 and sys.argv[1] == "server":
    #     address = "localhost"
    #     servermode = True
    #     port = int(sys.argv[2])
    #     if len(sys.argv) == 4:
    #         dhgroup = int(sys.argv[3])
    # elif len(sys.argv) >= 3:
    #     servermode = False
    #     address = sys.argv[1]
    #     port = int(sys.argv[2])
    #     if len(sys.argv) == 4:
    #         dhgroup = int(sys.argv[3])
    # else:
    #     sys.exit("Server usage: python3 main.py 'server' port [dhgroup]\
    #     \nClient usage: python3 main.py address port [dhgroup]")

    # alice = DiffieHellman()
    # bob = DiffieHellman()
    # server = NetworkHandler("localhost", 8089, True, alice)
    # client = NetworkHandler("localhost", 8089, False, bob)
    # server.start()
    # client.start()
    #
    # client.send("Detta borde krypteras")
    # m = server.receive()
    # print(m)

    gui = GUI(None)

if __name__ == "__main__":
    main()
