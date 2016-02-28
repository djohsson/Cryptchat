#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading


class WriteThread(threading.Thread):

    def __init__(self, networkhandler, connection):
        super(WriteThread, self).__init__()
        self.networkhandler = networkhandler
        self.connection = connection
        self._stop = threading.Event()
        self.setDaemon(True)

    def run(self):
        while True:
            m = self.networkhandler.getoutmessage()
            self.connection.send(bytes(m, "utf8"))

    def stop(self):
        self._stop.set()
