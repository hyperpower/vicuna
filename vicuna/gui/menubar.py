# -*- coding: utf-8 -*-

import tkinter as tk

class Menubar(tk.Menu):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # display the menu
        self.master.config(menu=self)
        # self.pack()
        self.create_file_menu()

    def create_file_menu(self):
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing) 
        self.add_cascade(label="File", menu=filemenu)

    def donothing(self):
        print("hi there, everyone!")