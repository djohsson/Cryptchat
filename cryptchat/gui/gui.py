#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter


class GUI(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.grid()
        self.initialize()

    def initialize(self):
        self.grid()
        self.title("Cryptchat")

        self.text = tkinter.Text(self, height=25, width=50)
        self.text.grid(row=0, column=0, sticky="NW")
        self.text.pack()
        self.text.insert("1.0", "<23:56:01> [bob] what is up alice")
        self.text.config(state="disabled")

        self.entry = tkinter.Entry(self, width=50)
        self.entry.grid(row=2, column=0, sticky="SW")
        self.entry.pack()

        self.resizable(width=False, height=False)
        self.mainloop()
