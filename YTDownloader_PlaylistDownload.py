import time
import pytube
from pytube import YouTube
from pytube import Playlist
import YTDownloader_SelectStream

# url = "https://www.youtube.com/watch?v=z0-osPz5Yno&list=" \
#       "PLXO08fqT4FgAujJUFfL743359_Oqo8nPM&ab_channel=%D0%9F%" \
#       "D0%B0%D1%80%D0%B0%D0%BB%D0%B0%D0%B9%D0%9F%D0%B8"


# Define Playlist Downloader:
def startPlaylistDownload(url):
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
            downloadVideo.streams.get_highest_resolution().download()

            print("success!")
            count = count + 1
    except:
        print("Download Failed")
    print("Out of loop")


# startPlaylistDownload(url)