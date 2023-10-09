# This version uses the progress bar but can't update the bar
# only a single window is used here. The next version will include
# bar updates and more than one window will be used.
# folder specification is also necessary

import os
from os import path
import sys
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from pytube import YouTube
from datetime import datetime
from PIL import Image, ImageTk
from pathlib import Path

gui = Tk()


# Title:
gui.title("YouTube Video Downloader")

# Create Icon
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))
zip_file_path = path.join(app_path, 'yticon.png')  # absolute zip file path
print(zip_file_path)
photo = ImageTk.PhotoImage(file=zip_file_path)
gui.wm_iconphoto(False, photo)

# Create Geometry:
gui.geometry("650x200")

# Create Frames:
frame1 = LabelFrame(gui, text="Insert Video:")
frame1.grid(row=0, column=0)
frame2 = LabelFrame(gui, text="Download Information:")
frame2.grid(row=0, column=3)

# Provide Information:
label1 = Label(frame1, text="Insert video url below:")
label1.grid(row=1, column=0)
frame_info = Label(frame2, text="Download Progress:")
frame_info.grid(row=1, column=0)
mpb = ttk.Progressbar(frame2, orient=HORIZONTAL, length=200)
mpb.grid(row=2, column=0)
e = Entry(frame1, width=50, borderwidth=5)
e.grid(row=2, column=0)


def dl_complete():
    label2 = Label(frame2, text="Download Complete")
    label2.grid(row=4, column=0)


# download:
def dl():
    download_start_time = datetime.now()

    def downloadCallback(stream, chunk, bytes_remaining):
        global download_start_time
        seconds_since_download_start = (datetime.now() - download_start_time).total_seconds()
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        # percent = StringVar()
        percentage_of_completion = bytes_downloaded / total_size * 100
        speed = round(((bytes_downloaded / 1024) / 1024) / seconds_since_download_start, 2)
        seconds_left = round(((bytes_remaining / 1024) / 1024) / float(speed), 2)
        print("percentage_of_completion:", round(percentage_of_completion, 2), "%")
        print("seconds_since_download_start:", round(seconds_since_download_start, 2), "seconds")
        print("speed:", round(speed, 2), "Mbps")
        print("seconds_left:", round(seconds_left, 2), "seconds")
        print()
        mpb["value"] = percentage_of_completion
        # percent = str(int(percentage_of_completion))
        percentLabel = Label(frame2, textvariable="Percentage: " + str(percentage_of_completion) + "%")
        percentLabel.grid(row=3, column=1)
        frame2.update_idletasks()

    def main():
        global download_start_time
        chunk_size = 1024
        url = e.get()
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


Download_Button = Button(gui, text="Download!", bg="green", fg="white", command=dl)
Download_Button.grid(row=3, column=0)

gui.mainloop()
