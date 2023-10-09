from tkinter import *
from tkinter import ttk, font
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys
import pathlib
import pytube
from pytube import YouTube
from pytube import Playlist
from pytube import streams
import datetime
from datetime import datetime
import time
import customtkinter
import tkinter
import scrapetube

# URL:
url = "https://www.youtube.com/watch?v=-QWxJ0j9EY8&ab_channel=TheCodingBug"
# Create YouTube Object
ytObject = YouTube(url)
# count the streams:
stream_number = 0
for _ in ytObject.streams:
    print(_, "\n")
    stream_number = stream_number + 1
print(stream_number)

# Application:
app = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

radio_var = customtkinter.IntVar(app, 0)
text_var = customtkinter.StringVar(app, "value", "name")
print(text_var)


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
    ytObject.streams[radio_var.get()].download()
    print("downloaded")


count = 0
for _ in ytObject.streams:
    text_var = str(_)
    print(text_var)
    customtkinter.CTkRadioButton(master=app, text=text_var,
                                 command=radiobutton_event, variable=radio_var,
                                 value=count).grid(padx=10, pady=10, sticky=W)
    count = count + 1

app.mainloop()
