#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from time import localtime, strftime
from threading import Thread, Semaphore, Condition


class GUI(tkinter.Tk):

    def __init__(self, parent, nick, networkhandler):
        tkinter.Tk.__init__(self, parent)
        self.grid()
        self.title("Cryptchat")
        self.out_message = []

        self.text = TextArea(self, height=25, width=50, font=("Droid Sans Mono", 12))
        self.text.grid(row=0, column=0, sticky="NW")
        self.text.pack()

        self.entry = TextEntry(self, nick, 50, font=("Droid Sans Mono", 12))
        self.entry.grid(row=2, column=0, sticky="SW")
        self.entry.pack()

        self.out_sem = Semaphore(0)
        self.out_condition = Condition()
        self.app_condition = Condition()

        sthread = SendThread(self, networkhandler)
        rthread = ReceiveThread(self, networkhandler)
        sthread.start()
        rthread.start()

        self.resizable(width=False, height=False)
        self.mainloop()

    def appendstring(self, sender, string):
        self.app_condition.acquire()
        t = ["<", strftime("%H:%M:%S", localtime()), "> ", "[", sender, "] ", string, "\n"]
        self.text.appendstring("".join(t))
        self.app_condition.notifyAll()
        self.app_condition.release()

    def get_sendmessage(self):
        '''
        Called by SendThread
        '''
        self.out_sem.acquire()
        self.out_condition.acquire()
        m = self.out_message.pop(0)
        self.out_condition.notifyAll()
        self.out_condition.release()
        return m

    def queue_sendmessage(self, m):
        '''
        Called by TextEntry
        '''
        self.out_condition.acquire()
        self.out_message.append(m)
        self.out_sem.release()
        self.out_condition.notifyAll()
        self.out_condition.release()


class TextArea(tkinter.Text):

    def __init__(self, parent, height, width, font):
        tkinter.Text.__init__(self, parent, height=height, width=width, font=font)
        self.parent = parent
        self.config(state="disabled")

    def appendstring(self, string):
        self.config(state="normal")
        self.insert(tkinter.END, string)
        self.see(tkinter.END)
        self.config(state="disabled")


class TextEntry(tkinter.Entry):

    def __init__(self, parent, nick, width, font):
        tkinter.Entry.__init__(self, parent, width=width, font=font)
        self.parent = parent
        self.nick = nick
        self.bind("<Return>", self.actionperformed)

    def actionperformed(self, *args):
        string = self.get()
        if len(string) > 0:
            self.parent.appendstring(self.nick, string)
            self.parent.queue_sendmessage(" ".join([self.nick, string]))
            self.delete(0, tkinter.END)


class ReceiveThread(Thread):

    def __init__(self, gui, networkhandler):
        super(ReceiveThread, self).__init__()
        self.networkhandler = networkhandler
        self.gui = gui
        self.setDaemon(True)

    def run(self):
        while True:
            m = self.networkhandler.receive()
            splitted = m.split(" ", 1)
            self.gui.appendstring(splitted[0], splitted[1])


class SendThread(Thread):

    def __init__(self, gui, networkhandler):
        super(SendThread, self).__init__()
        self.networkhandler = networkhandler
        self.gui = gui
        self.setDaemon(True)

    def run(self):
        while True:
            m = self.gui.get_sendmessage()
            self.networkhandler.send(m)
