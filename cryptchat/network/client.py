#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(bytes("hello", "utf8"))
