from pytube import YouTube
import YouTubeObject

link = "https://www.youtube.com/watch?v=JMiW7IiA5mI&ab_channel=HeroAragoTV"
yt_1 = YouTube(link)

print('Title: ', yt_1.title, '\n',
      'Description: ', '\n', yt_1.description, '\n',
      'Author: ', yt_1.author, '\n',
      'thumbnail: ', '\n', yt_1.thumbnail_url, '\n',
      'length: ', yt_1.length, 'seconds', '\n',
      'views: ', yt_1.views)

videos = yt_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

print()
stream = int(input("Enter stream number to download: "))
videos[stream].download()
print('Successfully downloaded')

