#pip3 install pytube

import pytube
links=["https://www.youtube.com/watch?v=EOC2XOb8efw", "https://www.youtube.com/watch?v=5xNe2e12MRA"]
destination = "/home/sangee/Videos"

def downloadVideos(links):
    for link in links:
        yt = pytube.YouTube(link)
        stream = yt.streams.filter(res="1080p").first()
        stream.download(output_path = destination)
downloadVideos(links)

