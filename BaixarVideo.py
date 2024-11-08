from pytubefix import YouTube

url = "https://youtu.be/Uzh1cyFqwfw?si=t1wVlpiJONWG6YcT"

yt = YouTube(url)

print(yt.title)
print(yt.description)
print(yt.publish_date)
print(yt.views)


for stream in yt.streams:
    print(stream)

video = yt.streams.get_highest_resolution()
print(video.resolution)