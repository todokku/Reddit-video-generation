from time import time
start = time()
from redditComment import redditComment
from divideComment import divideComment
from drawImage import drawImage
from speak import speak
from makingVideo import makingVideo
from processSound import processSound
from moviepy.editor import *
end = time()
print('*********importing time: ', end-start)
#########################################################################
#initialize   
start = time()                                                     
subreddit_name = 'AskReddit'                                            
total_iterations = int(input('# of comments to pull?   '))
N = int(input('Nth post?   '))              
end = time()
print('*********initialize time: ', end-start)        
#########################################################################
#########################################################################
#get comments
start = time()
(post,authors_pre,comments_pre,total_iterations) = redditComment(subreddit_name,total_iterations,N)
end = time()
print('*********get comments: ', end-start)
#########################################################################
#########################################################################
#process comments - break each comment in list of strings (for replies)
start = time()
authors      =[]
comments    =[]
y_locations =[]
for i in range(total_iterations):
    author = str(authors_pre[i])
    word = comments_pre[i].replace('\n','')
    (comments_parts,y_location) = divideComment(word)
    authors.append(author)
    comments.append(comments_parts)
    y_locations.append(y_location)
#process post title    
(post_title, post_y_location) = divideComment(post.title)
end = time()
print('*********process comments: ', end-start)
#########################################################################
#########################################################################
#draw image (for replies)
start = time()
for x in range(len(comments)):    
    drawImage(x, authors[x], comments[x], y_locations[x])
#draw image (for post title)
drawImage(98,str(post.author),post_title,post_y_location)
end = time()
print('*********draw: ', end-start)
#########################################################################     
#########################################################################
#Chat for replies

start = time()
language ='en'
for x in range(len(comments)):
    for i in range(len(comments[x])):
        myText = comments[x][i]
        output = speak(myText,language)
        output.save('part' + str(x) + '-' + str(i)+'.mp3')
#Chat for intro
for i in range(len(post_title)):
        myText = post_title[i]
        output = speak(myText,language)
        output.save('part98' + str(i)+'.mp3')
end = time()
print('*********chat: ', end-start)
#########################################################################        
#########################################################################  
#Processing the pauses in the soundclips
start = time()
for i in range(len(post_title)):
        audio = AudioFileClip('part98' + str(i)+'.mp3') 
        audio = processSound(audio)   
        audio.write_audiofile('part98' + str(i)+'.mp3')
        audio.reader.close_proc()
        audio.close()

for x in range(len(comments)):
    for i in range(len(comments[x])):
        audio = AudioFileClip('part'+str(x) + '-' + str(i)+'.mp3')
        audio = processSound(audio)   
        audio.write_audiofile('part'+str(x) + '-' + str(i)+'.mp3')
        audio.reader.close_proc()
        audio.close()
end = time()
print('*********pause: ', end-start)
#########################################################################        
#########################################################################                                                                                     
#make video
start =time()
makingVideo(comments,post_title)
end = time()
print('*********stitch: ', end-start)
#########################################################################
#########################################################################
#this version of code creates videos w/o background music, if desired use the following code to overlay music
#clip.audio = CompositeAudioClip([clip.audio, new_audio])
