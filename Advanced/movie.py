#pip3 install pytube

import pytube
links=["https://www.youtube.com/watch?v=KfUExOXxU5Q", "https://www.youtube.com/watch?v=fu2slipA8O4"]
destination = "/home/sangee/Videos"

def downloadVideos(links):
    for link in links:
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        stream.download(output_path = destination)
downloadVideos(links)
