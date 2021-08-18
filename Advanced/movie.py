#pip3 install pytube

import pytube
import time
import datetime

links=["https://www.youtube.com/watch?v=10RnRpMj9Mg", "https://www.youtube.com/watch?v=bADu51CTF8g"]
destination = "/home/sangee/Videos"

def downloadVideos(links):
    resolutions = ["1080p", "720p", "480p", "360p"]
    for link in links:
        yt = pytube.YouTube(link)
        for resolution in resolutions:
            stream = yt.streams.filter(res=resolution).first()
            if stream is not None:
                break;
        startTime = time.time();
        print("Start Time for Download Link "+link+" "+str(datetime.datetime.now()))
        print("Download Started ".center(50,"*"))
        stream.download(output_path = destination)
        finishTime = time.time();
        print("Download finished ".center(50,"*"))
        print("Finish Time for Download Link "+link+" "+str(datetime.datetime.now()))
        interval = finishTime-startTime
        duration = str(round(interval/60,3)) +" Minutes " +str(round(interval%60,3))+ " Seconds"
        print(("Time taken for downloading "+link+" is "+duration).center(50,"*"))
downloadVideos(links)
