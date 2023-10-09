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
root.geometry("370x200")
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

        print(f"Fetching.. \"{video.title}\"..")
        label1 = Label(root, text="Fetching.." + video.title + "...")
        label1.grid(row=3, column=0)
        root.update()

        print(f"Fetching successful\n")
        label2 = Label(root, text="Fetching Successful")
        label2.grid(row=4, column=0)
        root.update()

        print(f"Information: \n"
              f"File size:" + str({round(video.filesize * 0.000001, 2)}) + "MegaBytes\n"
              f"Highest Resolution:" + str({video.resolution}) + "\n"
              f"Author: {yt.author}")
        file_size = str(round(video.filesize * 0.000001, 2))
        label4 = Label(root, text="Information: \n"
                                  "File size: " + file_size + "Megabytes\n"
                                  "Highest resolution: " + video.resolution + "\n"
                                  "Author:" + yt.author)
        label4.grid(row=6, column=0)
        root.update()

        print("Views: {:,}\n".format(yt.views))
        label5 = Label(root, text="Views: " + str(format(yt.views)))
        label5.grid(row=7, column=0)
        root.update()

        print(f"Downloading \"{video.title}\"..")
        label6 = Label(root, text="Downloading")
        label6.grid(row=8, column=0)

        root.update_idletasks()

        download_start_time = datetime.now()
        video.download()
        print(f"Download Completed!")
        dl_complete()

    main()


downloadButton = Button(root, text="Download", bg="green", fg="white", command=dl)
downloadButton.grid(row=2, column=0)
label3 = Label(root, text="Video Information")
label3.grid(row=5, column=0)

root.mainloop()
