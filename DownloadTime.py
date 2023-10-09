from pytube import YouTube
from datetime import datetime

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