# pip install ffmpeg moviepy
# videoo formats
# WMV (wmv, wma, asf*)
# OGG (ogg, oga, ogv, ogx)
# 3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
# MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
import moviepy.editor as mp

def extractaudio(videofile):
    my_clip = mp.VideoFileClip(videofile)
    my_clip.audio.write_audiofile(r"my_result.mp3")


def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

if __name__ == '__main__':
    extractaudio("../audio.3gpp")
    combine_audio("../video.mp4", "./my_result.mp3", "movie.mp4")
