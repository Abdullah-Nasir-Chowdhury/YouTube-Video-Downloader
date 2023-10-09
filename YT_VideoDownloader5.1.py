# This version makes use of custom tkinter:

from tkinter import *
from tkinter import ttk
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys
import pathlib
import pytube
from pytube import YouTube
import datetime
from datetime import datetime
import time
import customtkinter
import tkinter


def startDownload():
    print("Downloading...")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Downloaded!", text_color="Blue")
    except:
        finishLabel.configure(text="Oops! Something Went Wrong...", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))

    # Update Progress Percentage:
    progPerc.configure(text=per + "%")
    progPerc.update()

    # Update Progress Bar:
    progBar.set(float(percentage_of_completion) / 100)
    frame.update_idletasks()


# System Settings:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame:
app = customtkinter.CTk()
app.title("YouTube Downloader")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Adding UI elements:
title = customtkinter.CTkLabel(master=frame, text="Insert YouTube Video URL")
title.pack(padx=10, pady=10)

# Link Inputs:
url_var = tkinter.StringVar(frame)
link = customtkinter.CTkEntry(master=frame, placeholder_text="URL", textvariable=url_var)
link.pack(pady=10, padx=10)

# Finished Downloading:
finishLabel = customtkinter.CTkLabel(master=app, text="")
finishLabel.pack()

# Progress Percentage:
progPerc = customtkinter.CTkLabel(frame, text="0%")
progPerc.pack()

progBar = customtkinter.CTkProgressBar(frame, width=400)
progBar.set(0)
progBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(master=frame, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
