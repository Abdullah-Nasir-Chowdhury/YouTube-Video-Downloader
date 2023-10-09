# This version will allow the user to choose the download stream
# All functionalities of version 7 will be available here
# There will be two frames in the download stats window:
# One will display the information of the download,
# the other will display the progress.

# Hey, what if I played the Moonlight Sonata in the background

# Use updated import modules:
from tkinter import *
from tkinter import ttk, font

import pygame.mixer
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
import datetime
from datetime import datetime
import time
import customtkinter
import tkinter
import playsound
from playsound import *
from playsound import playsound
import pygame
from pygame import mixer

#  ///////////////////////// MUSIC SECTION /////////////////////////////////////:

# Initialized mixer:
mixer.init()

pygame.mixer.music.load(r"C:\Users\HP\Desktop\Library\MyAudios\MoonlightSonata.mp3")


def music_play():
    pygame.mixer.music.play()


def music_stop():
    pygame.mixer.music.stop()


music_play()


# /////////////////////// MUSIC SECTION ENDS //////////////////////////////////

# Define Individual Downloader
def startIndividualDownload():

    print("Downloading...")
    DownloadInformationLabel = customtkinter.CTkLabel(master=app, text="fetching...")
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

    def main():
        try:
            DownloadInformationLabel.configure(text="Downloading...", text_color="green")
            DownloadInformationLabel.update()
            ytLink = frame1_url.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            Video = ytObject.streams.get_highest_resolution()

            Video.download()

            print("Download Complete!")
            DownloadInformationLabel.configure(text="Success!", text_color="blue")
            DownloadInformationLabel.update()
        except:
            print("Download Failed :(")
            DownloadInformationLabel.configure(text="Failed to Download :(", text_color="red")
            DownloadInformationLabel.update()
        print("Process complete")
        time.sleep(2)
        IndividualDownload_Window.destroy()

        app.update_idletasks()
    main()


# Define Playlist Downloader:
def startPlaylistDownload():
    print("fetching....")
    # Scrape Tube:
    # videos = scrapetube.get_playlist(frame2_url.get())
    # print("fetched playlist")
    # print("downloading...")
    # for video in videos:
    #     print(video["videoId"])
    # print("download complete")
    try:

        # Provide url
        playlist = Playlist(frame2_url.get())
        # Get Playlist Length
        playlist_length = len(playlist)
        output = "".join(["Videos in playlist: ", str(playlist_length)])
        print(output)

        # Print url of videos in playlist
        count = 0
        for video in playlist.videos:
            print(playlist[count])
            count = count + 1

        # get only audio:
        count = 0
        for video in playlist.videos:
            output = "".join(["getting audio for video", str(count + 1), "..."])
            print(output)
            video.streams.get_audio_only().download()
            print("Success!")
            count = count + 1

        # get video:
        count = 0
        for video in playlist.videos:
            output = "".join(["getting video(", str(count + 1), ") from playlist"])
            print(output)
            video.streams.get_lowest_resolution().download()
            print("Success!")
            count = count + 1

        print("Successfully Downloaded Playlist")
    except:
        output = "".join("Download Failed...")
        print(output)
    print("Out of loop")


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
                                          command=startPlaylistDownload)
DownloadButton2.grid(row=2, padx=125, pady=10)

check_var = tkinter.StringVar(app, "on")


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())
    if check_var.get() == "on":
        music_play()
    else:
        music_stop()


checkbox = customtkinter.CTkCheckBox(master=app, text="Music", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

app.mainloop()

