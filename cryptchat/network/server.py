#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64).decode("utf8")
    if len(buf) > 0:
        print(buf)
