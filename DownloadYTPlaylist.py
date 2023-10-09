import pytube
from pytube import *
from pytube import YouTube
from pytube import Playlist
from pytube import query
from pytube import Caption
from pytube import CaptionQuery

# Provide url
playlist = Playlist("https://www.youtube.com/watch?v=MvzK9Oguxcg&list=PLpMixYKO4EXcKoRTvN0FdNaUNobV0QGFQ&index=5&ab_channel=Atlas")

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
    output = "".join(["getting audio for video", str(count+1), "..."])
    print(output)
    video.streams.get_audio_only().download()
    print("Success!")
    count = count + 1

# get video:
count = 0
for video in playlist.videos:
    output = "".join(["getting video(", str(count+1), ") from playlist"])
    print(output)
    video.streams.get_lowest_resolution().download()
    print("Success!")
    count = count + 1

print("Successfully Downloaded Playlist")
