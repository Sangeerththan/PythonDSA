#pip3 install pytube

import pytube
link="https://www.youtube.com/watch?v=0T_1RrlaeJo"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
