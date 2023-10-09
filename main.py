from pytube import YouTube
from datetime import datetime
from DownloadTime import downloadCallback

download_start_time = datetime.now()


def main():
    global download_start_time
    chunk_size = 1024
    url = "https://youtu.be/BBnomwpF_uY"
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


main()
