# pip3 install pytube
# Todo: download non you tube video
import datetime
import os
import time

import pyperclip
import pytube
import wget
import re

from FileOperations import move_files, progress_function

links = []
destination = "/home/sangee/Videos"
movingDirectory = "/home/sangee/Videos/Projects/Java"


# movingDirectory = "/home/sangee/Videos/Projects/Python"


def download_videos(_links, youtube=False):
    resolutions = ["1080p", "720p", "480p", "360p"]
    count = 0
    for link in _links:
        if youtube:
            yt = pytube.YouTube(link, on_progress_callback=progress_function)
            yt.register_on_progress_callback(progress_function)
            for resolution in resolutions:
                stream = yt.streams.filter(progressive=True, res=resolution).first()
                if stream is not None:
                    break;
            start_time = time.time()
            print("Start Time for Download Link " + link + " " + str(datetime.datetime.now()))
            print("Download Started ".center(50, "*"))
            stream.download(output_path=destination)
            finish_time = time.time();
            print("Download finished ".center(50, "*"))
            print("Finish Time for Download Link " + link + " " + str(datetime.datetime.now()))
            interval = finish_time - start_time
            duration = str(round(interval / 60, 3)) + " Minutes " + str(round(interval % 60, 3)) + " Seconds"
            print(("Time taken for downloading " + link + " is " + duration).center(50, "*"))
        # This is incomplete and currently not working
        else:
            print("Downloading Non Youtube File".center(70, "*"))
            # getting video
            count += 1
            wget.download(link, os.path.join(destination, str(count) + ".mp4"))
            print("Finished Downloading Non Youtube File".center(70, "*"))


def main():
    youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
    ''', re.VERBOSE)
    # Downloading without duplicated links
    download_limit = int(input("Enter links count: "))
    while True:
        copied_link = str(pyperclip.paste())
        # print("youtube regex is:"+str(youtube_regex.findall(copied_link)))
        match = youtube_regex.match(copied_link)
        if match is not None:
            print(copied_link)
            links.append(copied_link)
        if len(links) >= download_limit:
            break
    unique_links = list(set(links))
    download_videos(unique_links, True)

    # check whether directory is present
    if not os.path.exists(movingDirectory):
        os.makedirs(movingDirectory)

    print(("Files are copied from " + destination + " to " + movingDirectory).center(70, "*"))
    # moving downloads to directory
    move_files(destination, movingDirectory)


if __name__ == '__main__':
    main()