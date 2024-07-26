
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
 
try:   
    os.system('cls') 
    yt = YouTube("https://www.youtube.com/watch?v=qnUJ7ySmwHg", on_progress_callback = on_progress)
    print('loading... ' + yt.title)
    
    ys = yt.streams.get_audio_only()
    path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    ys.download(mp3=True, output_path= path) 
except Exception as e:
    print("ERRO:", e)

    