#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from threading import Semaphore, Condition
from readthread import ReadThread
from writethread import WriteThread
from testthread import TestThread


class NetworkHandler():

    def __init__(self, address, port, servermode):
        self.in_message = []
        self.in_condition = Condition()
        self.in_sem = Semaphore(0)

        self.out_message = []
        self.out_condition = Condition()
        self.out_sem = Semaphore(0)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if servermode:
            self.socket.bind((address, port))
            self.socket.listen(5)
            self.connection, self.clientaddress = self.socket.accept()
        else:
            self.socket.connect((address, port))

        self.readthread = ReadThread(self, self.connection)
        self.testthread = TestThread(self)
        self.writethread = WriteThread(self, self.connection)
        self.writethread.start()
        self.readthread.start()
        self.testthread.start()

    def receive(self, m):
        '''
        Called by readthread
        '''
        self.in_condition.acquire()
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
        self.out_message.append(m)
        self.out_sem.release()
        self.out_condition.notifyAll()
        self.out_condition.release()

    def getoutmessage(self):
        '''
        Called by writethread
        '''
        self.out_sem.acquire()
        self.out_condition.acquire()
        m = self.out_message.pop(0)
        self.out_condition.notifyAll()
        self.out_condition.release()
        return m
