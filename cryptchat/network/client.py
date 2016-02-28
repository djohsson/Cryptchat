#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# THIS MODULE WILL BE REMOVED. HERE FOR TESTING PURPOSES
#
#

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8089))
while True:
    string = input("")
    s.send(bytes(string, "utf8"))
