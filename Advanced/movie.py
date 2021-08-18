#pip3 install pytube

import pytube
import time
import datetime
import shutil
import os

links=[
      "https://www.youtube.com/watch?v=yZvFH7B6gKI",
      "https://www.youtube.com/watch?v=_XbttSk3ALs"
      ]
destination = "/home/sangee/Videos"
movingDirectory = "/home/sangee/Videos/DataAnalytics"

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

def movedownloads(src, dest):
    files = os.listdir(src)
    for f in files:
        filePath = os.path.join(src, f)
        print(("copying file"+str(f)).center(70,"#"))
        if os.path.isfile(filePath) and os.path.isdir(dest):
            print(("Moving file"+str(f)).center(70,"#"))    
            print(filePath)       
            shutil.move(filePath, dest)


#Downloading the links
downloadVideos(links)

#check whether directory is present
if not os.path.exists(movingDirectory):
    os.makedirs(movingDirectory)
print(movingDirectory)
#moving downloads to directory
movedownloads(destination, movingDirectory)