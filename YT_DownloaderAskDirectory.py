import customtkinter
import tkinter
from tkinter import *
from customtkinter import *
from tkinter import filedialog

# fileDir_DialogBox_window = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


def fileDir():
    my_dir = filedialog.askdirectory()
    path = r'{}'.format(my_dir)
    print(path)

    return path


# test_output = ""
# fileDir(test_output)
# print(test_output)

# fileDir_DialogBox_window.mainloop()


