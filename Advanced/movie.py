#pip3 install pytube

import pytube
link="https://www.youtube.com/watch?v=gR-tJhoO4i0&list=PL4QNnZJr8sRNiuUBUvMJ7b4eQJotYO2mo"
destination = "/home/sangee/Videos"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(output_path = destination)
