import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import urllib
from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
from time import strftime
import pyttsx3
from googlesearch import search

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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
            
def Assistant(command):

    #Name
    if 'your name' in command:
        speak('my name is alexa')

    #greetings
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            speak('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            speak('Hello Sir. Good afternoon')
        else:
            speak('Hello Sir. Good evening')
    #Time
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

    #Shutdown
    elif 'shutdown' in command:
        speak('Bye bye Sir. Have a nice day')
        sys.exit()

    #launch
    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            speak('I have launched the desired application')

    #open Website
    elif 'open' in command:
        name = command.split('open')[1]
        if name: 
            Website=str('www.')+name+str('.com')
            webbrowser.open(Website)

    #search Something
    elif 'search' in command:
        name = command.split('search')[1]
        if name: 
            for j in search(query, tld="co.in", num=10, stop=1, pause=2):
                webbrowser.open(Website)

    #play video from Youtube       
    elif 'play' in command:
        name = command.split('play')[1]
        if 'song' not in name:
            name=name+str('song')
        for j in search(name, tld="co.in", num=10, stop=10, pause=2,tpe='vid'):
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
    #joke
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')

    #top stories from google news
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:15]:
                speak(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
    #current weather
    elif 'current weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    #Ask me anything
    elif 'tell me about' in command:
        name = command.split('about')[1]
        ny = wikipedia.page(topic)
        speak(ny.content[:500].encode('utf-8'))
        
while(1):
    command=listen()
    if command=='alexa':
        speak("hi i am your voice assistant")
        speak("what can i do for you")
        print("hi i am your voice assistant")
        print("what can i do for you")
        command=listen()
        Assistant(command)

