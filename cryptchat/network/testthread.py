#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# THIS MODULE WILL BE REMOVED. HERE FOR TESTING PURPOSES
#
#

import socket
import threading

RECV_BUFFER = 2048

class TestThread(threading.Thread):
    global RECV_BUFFER

    def __init__(self, networkhandler):
        self.networkhandler = networkhandler
        threading.Thread.__init__(self)

    def run(self):
        while True:
            m = self.networkhandler.getinmessage()
            print("test: " + m)
