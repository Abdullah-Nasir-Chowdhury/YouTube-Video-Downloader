import YT_VidDownloadedGIF
from pytube import YouTube
import pytube

YT_VidDownloadedGIF.vidDownloadSuccessGIF()
url = "https://www.youtube.com/watch?v=vVRrOi5LGSo&list=PLpMixYKO4EXcKoRTvN0FdNaUNobV0QGFQ&index=13&ab_channel=Atlas"
ytobj = YouTube(url)
print(ytobj)