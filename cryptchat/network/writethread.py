#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading


class WriteThread(threading.Thread):

    def __init__(self, networkhandler, connection):
        super(WriteThread, self).__init__()
        self.networkhandler = networkhandler
        self.connection = connection
        self.setDaemon(True)

    def run(self):
        while True:
            m = self.networkhandler.getoutmessage()
            self.connection.send(bytes(m, "utf8"))
