# v9.2 came with an almost proper video downloader
# but the information about the download was missing
# the playlist downloader was meh...

# To improve the playlist download:
# 1. The video url list will be taken from the playlist and saved within a list
# 2. The list will be run within a for loop and the videos within that list will
#     be downloaded individually using the individualDownload function
# 3. A progress bar will be provided depending on the list completion
# 4. Per download the progress bar will be updated
# 5. There will also be the video download progress bar
# 6. Information about the videos downloaded will also be available

# 9.1 was good, but the download progress bar is always on top
# kindly start the download progress bar after the download starts

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
import YT_DownloaderAskDirectory
import YTDownloader_SelectStream
import YTDownloader_PlaylistDownload
import YTDownloader_PlaylistDownloaderWindow

#  ///////////////////////// MUSIC SECTION /////////////////////////////////////:

# Initialized mixer:
mixer.init()

pygame.mixer.music.load(r"C:\Users\HP\Desktop\Library\MyAudios\MoonlightSonata.mp3")


def music_play():
    pygame.mixer.music.play(-1)


def music_stop():
    pygame.mixer.music.stop()


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())
    if check_var.get() == "on":
        music_play()
    else:
        music_stop()


music_play()


# /////////////////////// MUSIC SECTION ENDS //////////////////////////////////


# Define Individual Downloader
def startIndividualDownload():

    print("Downloading...")

    def main():

        try:
            ytLink = frame1_url.get()
            DownloadInformationLabel = customtkinter.CTkLabel(master=app, text="fetching...", text_color="grey")
            DownloadInformationLabel.grid(row=3, padx=10, pady=10)
            DownloadInformationLabel.after(2000, DownloadInformationLabel.destroy())
            YTDownloader_SelectStream.Streams_scrollbar(ytLink, app)
        except:
            DownloadInformationLabel.grid_remove()
            print("Download Failed :(")
            DownloadFailedLabel = customtkinter.CTkLabel(master=app, text="Failed :(", text_color="red")
            DownloadFailedLabel.grid(row=3, padx=10, pady=10)

            # Display Fail GIF:
            YT_DownloaderGIFs.vidDownloadFailedGIF()

        print("Process complete")

        app.update_idletasks()
    main()


def PlaylistDownload():
    YTDownloader_PlaylistDownload.startPlaylistDownload(frame2_url.get())


# Main Application:
app = customtkinter.CTk()
app.title("YouTube Video Downloader")
app.geometry("1000x400")

# Create Appearance:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# Create Frames for individual and play-list downloads:
# Frame1:
frame1 = customtkinter.CTkFrame(master=app, width=400)
frame1.grid(padx=50, pady=20, row=1, column=0)
# Don't allow frame to shrink or grow when grid is used:
frame1.grid_propagate(False)

# Frame2:
frame2 = customtkinter.CTkFrame(master=app, width=400)
frame2.grid(padx=50, pady=20, row=1, column=1)
# Don't allow frame to shrink or grow when grid is used:
frame2.grid_propagate(False)


# Welcome Text:
welcome = customtkinter.CTkLabel(master=app, text="YouTube Video Downloader", font=("", 24))
welcome.grid(row=0, column=0, columnspan=2, pady=20)


# Create UI for frame1:
# Intro:
frame1_introduction = customtkinter.CTkLabel(master=frame1, text_color="grey", text="Download individual video")
frame1_introduction.grid(padx=125, pady=10)
# URL:
frame1_URL = customtkinter.StringVar(master=frame1)
frame1_url = customtkinter.CTkEntry(master=frame1, textvariable=frame1_URL, placeholder_text="URL")
frame1_url.grid(row=1, padx=125, pady=10)
# DownloadButton:
DownloadButton1 = customtkinter.CTkButton(master=frame1, text="Download!", command=startIndividualDownload)
DownloadButton1.grid(row=2, padx=125, pady=10)


# Create UI for frame2:
frame2_introduction = customtkinter.CTkLabel(master=frame2, text_color="grey", text="Download playlist")
frame2_introduction.grid(padx=125, pady=10)
# URL:
frame2_URL = customtkinter.StringVar(master=frame2)
frame2_url = customtkinter.CTkEntry(master=frame2, textvariable=frame2_URL, placeholder_text="URL")
frame2_url.grid(row=1, padx=125, pady=10)
# DownloadButton:
DownloadButton2 = customtkinter.CTkButton(master=frame2, text="Download!",
                                          fg_color=("pink", "magenta"),
                                          hover=True, hover_color="purple",
                                          command=PlaylistDownload)
DownloadButton2.grid(row=2, padx=125, pady=10)

check_var = tkinter.StringVar(app, "on")

checkbox = customtkinter.CTkCheckBox(master=app, text="Music", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

app.mainloop()

