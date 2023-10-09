# Use updated import modules:
from tkinter import *
from tkinter import ttk, font
import pygame.mixer
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image as PIM, ImageTk
import os
import sys
import pathlib
import pytube
from pytube import YouTube
from pytube import Playlist
import datetime
from datetime import datetime
import time
import customtkinter
import tkinter
import pygame
from pygame import mixer
import YT_DownloaderGIFs
import YT_DownloaderSelectStream


# Define Individual Downloader
def startIndividualDownload(app):
    print("Downloading...")
    DownloadInformationLabel = customtkinter.CTkLabel(master=app, text="fetching...", text_color="grey")
    DownloadInformationLabel.grid(row=3, padx=10, pady=10)
    # Download Progress Bar Window:
    IndividualDownload_Window = customtkinter.CTkToplevel()
    IndividualDownload_Window.lift()
    IndividualDownload_Window.wm_positionfrom()
    IndividualDownload_Window.attributes("-topmost", True)
    IndividualDownload_Window.title("Download Stats")
    x = app.winfo_x()
    y = app.winfo_y()
    IndividualDownload_Window.geometry("+%d+%d" % (x + 200, y + 200))

    # Set Progress:
    progressPercentage = customtkinter.CTkLabel(master=IndividualDownload_Window, text="0%")
    progressPercentage.pack(padx=10, pady=10)
    progressBar = customtkinter.CTkProgressBar(master=IndividualDownload_Window, width=300)
    progressBar.set(0)
    progressBar.pack(padx=10, pady=10)

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

        IndividualDownload_Window.update_idletasks()

