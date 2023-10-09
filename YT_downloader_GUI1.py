from tkinter import *
from pytube import YouTube
from datetime import datetime
from PIL import Image, ImageTk

gui = Tk()

# Title:
gui.title("YouTube Video Downloader")

# Create Icon
# photo = ImageTk.PhotoImage(file=r"yticon.png")
# gui.wm_iconphoto(False, photo)

# Provide Information:
label1 = Label(gui, text="Insert video url below:", padx=100)
label1.grid(row=0, column=0)

e = Entry(gui, width=50, borderwidth=5)
e.grid(row=1, column=0)


def dl_complete():
    label2 = Label(gui, text="Download Complete")
    label2.grid(row=4, column=0)


# download:
def dl():
    download_start_time = datetime.now()

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
