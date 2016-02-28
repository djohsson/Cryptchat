#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

RECV_BUFFER = 2048

class ReadThread(threading.Thread):
    global RECV_BUFFER

    def __init__(self, networkhandler, connection):
        self.connection = connection
        self.networkhandler = networkhandler
        threading.Thread.__init__(self)

    def run(self):
        while True:
            m = self.connection.recv(RECV_BUFFER)
            if len(m) > 0:
                self.networkhandler.receive(m.decode("utf8"))
