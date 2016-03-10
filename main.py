#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from cryptchat.crypto.diffiehellman import DiffieHellman
from cryptchat.network.networkhandler import NetworkHandler
from cryptchat.gui.gui import GUI


def main():
    if len(sys.argv) >= 4:
        nick = sys.argv[1]
        servermode = True
        address = "localhost"
        if sys.argv[2] != "server":
            servermode = False
            address = sys.argv[2]
        port = int(sys.argv[3])
        if len(sys.argv) == 5:
            dhgroup = sys.argv[4]
        else:
            dhgroup = 17
    else:
        sys.exit("Server usage: python3 main.py nick 'server' port [dhgroup]\
        \nClient usage: python3 main.py nick address port [dhgroup]")

    dh = DiffieHellman(dhgroup)
    net = NetworkHandler(address, port, servermode, dh)
    net.start()
    gui = GUI(None, nick, net)

if __name__ == "__main__":
    main()
