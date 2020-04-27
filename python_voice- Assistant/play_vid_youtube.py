import pafy
import vlc
from googlesearch import search
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        try:
            r.adjust_for_ambient_noise(source) 
            print ("Say Something")
            audio = r.listen(source) 
            text = r.recognize_google(audio).lower() 
            print('You said: ' +text)
            return(text)
        except sr.UnknownValueError:
            print('....')
            listen()
            

command=listen()
if 'play' in command:
    command=command.split('play')[1]
    for j in search(name, tld="co.in", num=10, stop=1, pause=2,tpe='vid'):
        video = pafy.new(j)
        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        command=listen()
        if 'pause' in command:
            player.pause()
        elif 'resume' in command:
            player.resume()
        elif 'stop' in command:
            player.stop()
        
