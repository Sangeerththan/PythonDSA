#pip3 install pytube

import pytube
import time
import datetime

links=["https://www.youtube.com/watch?v=EOC2XOb8efw", "https://www.youtube.com/watch?v=5xNe2e12MRA"]
destination = "/home/sangee/Videos"

def downloadVideos(links):
    for link in links:
        yt = pytube.YouTube(link)
        stream = yt.streams.filter(res="1080p").first()
        startTime = time.time();
        print("Start Time for Download Link "+link+" "+str(datetime.datetime.now()))
        print("Download Started "+link)
        stream.download(output_path = destination)
        finishTime = time.time();
        print("Download finished "+link)
        print("Finish Time for Download Link "+link+" "+str(datetime.datetime.now()))
        print("Time taken for downloading "+link+" is "+str(finishTime-startTime))
downloadVideos(links)
