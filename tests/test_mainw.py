import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vicuna.gui.mainw import Application
import tkinter as tk


root = tk.Tk()
app = Application(master=root)
app.master.title("My Do-Nothing Application")
app.master.minsize(500, 400)
app.mainloop()