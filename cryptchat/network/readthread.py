#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

RECV_BUFFER = 2048

class ReadThread(threading.Thread):
    global RECV_BUFFER

    def __init__(self, networkhandler, connection):
        super(ReadThread, self).__init__()
        self.networkhandler = networkhandler
        self.connection = connection
        self.setDaemon(True)

    def run(self):
        while True:
            m = self.connection.recv(RECV_BUFFER).decode("utf8")
            if len(m) > 0:
                self.networkhandler.receive(m)
