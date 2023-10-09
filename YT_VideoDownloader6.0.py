# There's  only a single window in v5.1
# Progress Bar and text don't change values after reaching 100%
# This version solves those problems:

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
    # Download Progress Bar Window:
    window = customtkinter.CTkToplevel()
    window.title("Download Stats")

    # Set Progress:
    progressPercentage = customtkinter.CTkLabel(master=window, text="0%")
    progressPercentage.pack(padx=10, pady=10)
    progressBar = customtkinter.CTkProgressBar(master=window, width=300)
    progressBar.set(0)
    progressBar.pack(padx=10, pady=10)

    print("Downloading...")
    DownloadInformationLabel = customtkinter.CTkLabel(master=app, text="fetching...")
    DownloadInformationLabel.pack(padx=10, pady=10)

    def on_progress(stream, chunk, bytes_remaining):

        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        print(percentage_of_completion)
        str_percentage_of_completion = str(int(percentage_of_completion))

        # Update Progress:
        progressPercentage.configure(text=str_percentage_of_completion + "%")
        progressPercentage.update()

        progressBar.set(float(percentage_of_completion) / 100)
        progressBar.update()

        window.update_idletasks()

    def main():
        try:
            ytLink = url.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            Video = ytObject.streams.get_highest_resolution()
            DownloadInformationLabel.configure(text="Downloading...", text_color="green")
            DownloadInformationLabel.update()

            Video.download()

            print("Download Complete!")
            DownloadInformationLabel.configure(text="Success!", text_color="blue")
            DownloadInformationLabel.update()
        except:
            print("Download Failed :(")
            DownloadInformationLabel.configure(text="Failed to Download :(", text_color="red")
            DownloadInformationLabel.update()
        print("Process complete")
        processCompleteLabel = customtkinter.CTkLabel(master=app, text="Insert Next URL", text_color="blue")
        processCompleteLabel.pack(padx=10, pady=10)
        time.sleep(2)
        window.destroy()

        app.update_idletasks()
    main()


# Create Appearance:
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("System")

# Application Main frame:
app = customtkinter.CTk()
app.title("YouTube Video Downloader v6.0")
frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=60, pady=20, fill="both", expand=True)

# Application UI:
welcome_text = customtkinter.CTkLabel(master=frame, text="Insert Video URL below:")
welcome_text.pack(padx=10, pady=10)

url_var = tkinter.StringVar(frame, "")
url = customtkinter.CTkEntry(master=frame, textvariable=url_var)
url.pack()

# Download Button:
downloadButton = customtkinter.CTkButton(master=frame, text="Download", command=startDownload)
downloadButton.pack(padx=10, pady=10)

app.mainloop()
