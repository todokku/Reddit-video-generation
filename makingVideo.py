from moviepy.editor import *

def makingVideo(comments,post_title):
    videos=[]
    flash = VideoFileClip('flash.mp4')
    flash.fps = 30
    for i in range(len(post_title)):
        audio = AudioFileClip('part98' + str(i)+'.mp3')
        intro = ImageClip('part98' + '-' + str(i)+'.jpg', duration = audio.duration )
        intro.fps = 30
        intro = intro.set_audio(audio)
        intro = intro.set_end(intro.duration-.3)
        videos.append(intro)
    videos.append(flash)
    
    for x in range(len(comments)):
        for i in range(len(comments[x])):
            audio = AudioFileClip('part'+str(x) + '-' + str(i)+'.mp3')
            clip = ImageClip('part'+str(x) + '-' + str(i)+'.jpg', duration = audio.duration )
            clip.fps = 30
            clip = clip.set_audio(audio)
            clip = clip.set_end(clip.duration-.3)
            videos.append(clip)
        videos.append(flash)
    final_clip = concatenate(videos)
    final_clip.write_videofile("final.mp4")



