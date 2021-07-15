from pytube import YouTube
from pytube.cli import on_progress
from pydub import AudioSegment 
from os import remove

def video(link):
    yt = YouTube(link , on_progress_callback=on_progress) #URL + on_progress mostra o andamento do download.
    print(f'{yt.title}.mp4 ') #titulo do video
    stream = yt.streams.first()  #escolhe a primeira opção de media format para download
    stream.download('Downloads/') #caminho para pasta download
    print("\033[1;32mDownload concluido!\033[m")

def audio(link):
    yt = YouTube(link , on_progress_callback=on_progress) #URL + on_progress mostra o andamento do download.
    print(f'{yt.title}.mp3 ') #titulo do video
    stream = yt.streams.filter(only_audio=True).first() #escolhe a primeira opção de media format para download
    stream.download('Downloads/') #caminho para pasta download

    audio = 'Downloads/' + yt.streams[0].default_filename #pasta + nome do video.mp4
    converter = AudioSegment.from_file(audio, format="mp4") #audio = nomedovideo.mp4
    remove(audio) #remove arquivo mp4
    audio = audio.replace('.mp4','.mp3') #substitue o nomevideo.mp4 da variavel por nomevideo.mp3
    converter.export(audio, format="mp3") #audio = nomedovideo.mp3
   
    print("\033[1;32mDownload concluido!\033[m")


while True:
    escolha = input("mp3 ou mp4? ").lower()
    if escolha == 'mp3':
        audio(str(input("Link: ")))
    elif escolha == 'mp4':
        video(str(input("Link: ")))
    else:
        print("Formato não encontrado!")
    
