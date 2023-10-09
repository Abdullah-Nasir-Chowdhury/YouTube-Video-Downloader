# Proper use of custom tkinter with download progress and
# download stats

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

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("System")

custom_gui = customtkinter.CTk()
# custom_gui.geometry("500x500")
custom_gui.title("YT_Video Downloader v5.0")

frame = customtkinter.CTkFrame(master=custom_gui)
frame.pack(pady=20, padx=60, fill="both", expand=True)

cLabel = customtkinter.CTkLabel(master=frame, text="Download YouTube Videos!")
cLabel.pack(pady=12, padx=10)

# cLabel1 = customtkinter.CTkLabel(master=custom_gui, text="Enter URL:")
# cLabel1.pack(pady=12, padx=10)
cEntry = customtkinter.CTkEntry(master=frame, placeholder_text="URL")
cEntry.pack(pady=12, padx=10)


def dl():
    download_start_time = datetime.now()
    new_window = customtkinter.CTkToplevel()
    new_window.title("Download Stats")

    def downloadCallback(stream, chunk, bytes_remaining):
        global download_start_time
        seconds_since_download_start = (datetime.now() - download_start_time).total_seconds()
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        speed = round(((bytes_downloaded / 1024) / 1024) / seconds_since_download_start, 2)
        seconds_left = round(((bytes_remaining / 1024) / 1024) / float(speed), 2)
        print("percentage_of_completion:", round(percentage_of_completion, 2), "%")
        print("seconds_since_download_start:", round(seconds_since_download_start, 2), "seconds")
        print("speed:", round(speed, 2), "Mbps")
        print("seconds_left:", round(seconds_left, 2), "seconds")
        print()

        new_window_label1 = customtkinter.CTkLabel(master=new_window, text="Download Progress:")
        new_window_label1.grid(row=0, column=0)
        progress_bar = ttk.Progressbar(new_window, orient=HORIZONTAL, length=200)
        progress_bar["value"] = percentage_of_completion
        progress_bar.grid(row=0, column=1)
        new_window.update_idletasks()

    def dl_complete():
        window_3 = customtkinter.CTkToplevel()
        label_window_3 = customtkinter.CTkLabel(master=window_3, text="Download Complete")
        label_window_3.grid(row=2, column=0)

    def main():
        global download_start_time
        chunk_size = 1024
        url = cEntry.get()
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        yt.register_on_progress_callback(downloadCallback)

        print(f"Fetching.. \"{video.title}\"..")
        # label1 = customtkinter.CTkLabel(master=custom_gui, text="Fetching.." + video.title + "...")
        # label1.grid(row=3, column=0)

        print(f"Fetching successful\n")
        # label2 = customtkinter.CTkLabel(master=custom_gui, text="Fetching Successful")
        # label2.grid(row=4, column=0)

        print(f"Information: \n"
              f"File size:" + str({round(video.filesize * 0.000001, 2)}) + "MegaBytes\n"
              f"Highest Resolution:" + str({video.resolution}) + "\n"
              f"Author: {yt.author}")
        file_size = str(round(video.filesize * 0.000001, 2))
        # label4 = customtkinter.CTkLabel(master=custom_gui, text="Information: \n"
        #                                                         "File size: " + file_size + "Megabytes\n"
        #                                                         "Highest resolution: " + video.resolution + "\n"
        #                                                         "Author:" + yt.author)
        # label4.grid(row=6, column=0)

        print("Views: {:,}\n".format(yt.views))
        # label5 = customtkinter.CTkLabel(master=custom_gui, text="Views: " + str(format(yt.views)))
        # label5.grid(row=7, column=0)

        print(f"Downloading \"{video.title}\"..")
        # label6 = customtkinter.CTkLabel(master=custom_gui, text="Downloading")
        # label6.grid(row=8, column=0)

        custom_gui.update_idletasks()

        download_start_time = datetime.now()
        video.download()
        print(f"Download Completed!")
        dl_complete()

    main()


download_button = customtkinter.CTkButton(master=frame, text="Download!", command=dl)
download_button.pack(pady=12, padx=10)

custom_gui.mainloop()
