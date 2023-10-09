# This version will have two windows and the download complete and progress bar will be updated

# Import modules:
from tkinter import *
from tkinter import ttk
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

# initialize root:
root = Tk()
root.geometry("400x400")
root.title("YouTube Downloader")
root.iconbitmap(r".\images\favicon.ico")

frame1 = LabelFrame(root, text="Insert video URL")
frame1.grid(row=0, column=0)
Label1_frame1 = Label(frame1, text="URL: ")
Label1_frame1.grid(row=0, column=0)
e1 = Entry(frame1, width=50)
e1.grid(row=0, column=1)


# download:
def dl():
    download_start_time = datetime.now()
    new_window = Toplevel()
    new_window.title("Stats")

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
        new_window_label1 = Label(new_window, text="Download Progress:")
        new_window_label1.grid(row=0, column=0)
        progress_bar = ttk.Progressbar(new_window, orient=HORIZONTAL, length=200)
        progress_bar["value"] = percentage_of_completion
        progress_bar.grid(row=0, column=1)
        # percentLabel = Label(new_window, textvariable="Percentage: " + str(percentage_of_completion) + "%")
        # percentLabel.grid(row=3, column=1)
        new_window.update_idletasks()

    def dl_complete():
        label2 = Label(new_window, text="Download Complete")
        label2.grid(row=2, column=0)

    def main():
        global download_start_time
        chunk_size = 1024
        url = e1.get()
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        yt.register_on_progress_callback(downloadCallback)
        print(f"Fetching \"{video.title}\"..")
        print(f"Fetching successful\n")
        print(f"Information: \n"
              f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
              f"Highest Resolution: {video.resolution}\n"
              f"Author: {yt.author}")
        print("Views: {:,}\n".format(yt.views))

        print(f"Downloading \"{video.title}\"..")

        download_start_time = datetime.now()
        video.download()
        print(f"Download Completed!")
        dl_complete()

    main()


downloadButton = Button(root, text="Download", command=dl)
downloadButton.grid(row=2, column=0)
root.mainloop()
