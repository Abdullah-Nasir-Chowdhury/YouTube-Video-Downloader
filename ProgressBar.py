# progress Bar:

import sys
from tkinter import *
from tkinter import ttk

Gui = Tk()

progressbar = ttk.Progressbar(Gui, orient="horizontal", length=200, mode="determinate")
progressbar.pack()
progressbar["maximum"] = 100
progressbar["value"] = 50


Gui.mainloop()
