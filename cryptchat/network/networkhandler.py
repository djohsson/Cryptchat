#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from threading import Semaphore, Condition, Thread
from .readthread import ReadThread
from .writethread import WriteThread
from .testthread import TestThread


class NetworkHandler():

    def __init__(self, address, port, servermode, dh, cipher):
        self.address = address
        self.port = port
        self.servermode = servermode
        self.dh = dh
        self.cipher = cipher

        self.in_message = []
        self.in_condition = Condition()
        self.in_sem = Semaphore(0)

        self.out_message = []
        self.out_condition = Condition()
        self.out_sem = Semaphore(0)

        self.threads = []
        self.starter = NetworkStarter(self)

        #self.exchangekeys()

    def start(self):
        self.starter.start()

    def initialize(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.servermode:
            self.socket.bind((self.address, self.port))
            self.socket.listen(5)
            self.connection, self.clientaddress = self.socket.accept()
        else:
            self.socket.connect((self.address, self.port))
            self.connection = self.socket

        self.readthread = ReadThread(self, self.connection)
        self.writethread = WriteThread(self, self.connection)
        self.threads.append(self.writethread)
        self.threads.append(self.readthread)
        self.writethread.start()
        self.readthread.start()

    def stop(self):
        for thread in self.threads:
            thread.stop()

    def receive(self, c):
        '''
        Called by readthread
        '''
        self.in_condition.acquire()
        m = self.cipher.decrypt(c)
        self.in_message.append(m)
        self.in_sem.release()
        self.in_condition.notifyAll()
        self.in_condition.release()

    def getinmessage(self):
        '''
        Called by user interface
        '''
        self.in_sem.acquire()
        self.in_condition.acquire()
        m = self.in_message.pop(0)
        self.in_condition.notifyAll()
        self.in_condition.release()
        return m

    def send(self, m):
        '''
        Called by user interface
        '''
        self.out_condition.acquire()
        c = self.cipher.encrypt(m)
        self.out_message.append(c)
        self.out_sem.release()
        self.out_condition.notifyAll()
        self.out_condition.release()

    def getoutmessage(self):
        '''
        Called by writethread
        '''
        self.out_sem.acquire()
        self.out_condition.acquire()
        c = self.out_message.pop(0)
        self.out_condition.notifyAll()
        self.out_condition.release()
        return c

    def exchangekeys(self):
        #TODO
        #self.send(key)
        #b = self.receive(key)
        #sessionkey = dh.gensessionkey(b)
        return

class NetworkStarter(Thread):
    def __init__(self, net):
        super(NetworkStarter, self).__init__()
        self.net = net
        self.setDaemon(True)

    def run(self):
        self.net.initialize()
