import customtkinter
from customtkinter import *
from PIL import Image as PIM, ImageTk
import os
import sys
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pygame
from pygame import mixer
import YT_DownloaderGIFs
import YTDownloader_SelectStream
import YT_DownloaderAskDirectory
from pytube import YouTube
from pytube import Playlist


# Define Playlist Downloader:
def startPlaylistDownload(url):
    PlaylistDownloader_Window = customtkinter.CTk()
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    DownloadInfo_Label = customtkinter.CTkLabel(master=PlaylistDownloader_Window, text="Now Downloading:",
                                                font=("", 24))
    DownloadInfo_Label.grid(row=1, column=0, padx=10, pady=10, sticky=N + S)
    # DownloadInfo_Label.place(relx=0.5, rely=0.5)

    DownloadInfo_Frame = customtkinter.CTkScrollableFrame(master=PlaylistDownloader_Window,
                                                          width=400, height=500,
                                                          corner_radius=10,
                                                          label_text="Download Information",
                                                          label_text_color="gray")
    DownloadInfo_Frame.grid(row=0, column=1, rowspan=5)

    print("fetching....")

    try:

        # Provide url
        playlist = Playlist(url)
        # Get Playlist Length
        playlist_length = len(playlist)
        output = "".join(["Videos in playlist: ", str(playlist_length)])
        print(output)

        # Print url of videos in playlist
        count = 0
        for _ in playlist.videos:
            print(playlist[count])
            downloadVideo = YouTube(playlist[count])
            print(downloadVideo.title)
            customtkinter.CTkLabel(master=PlaylistDownloader_Window,
                                   text=downloadVideo.title).grid(row=2, column=0)
            downloadVideo.streams.get_highest_resolution().download()

            print("success!")
            count = count + 1
    except:
        print("Download Failed")
        customtkinter.CTkLabel(master=PlaylistDownloader_Window,
                               text="Download failed",
                               text_color="red").grid(row=3, column=0)

    print("Out of loop")

    PlaylistDownloader_Window.mainloop()
