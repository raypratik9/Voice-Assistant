import webbrowser
import speech_recognition as sr 
import pyttsx3

##################################Speak########################################
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

###############################################################################
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")
Website=""
# to search 
query = "sensors used in arduino"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
    Website=j
    
#webbrowser.open(Website)
#############################################################################
from urllib.request import Request, urlopen
url="https://stackoverflow.com/search?q=html+error+403"
req = Request(Website, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
#print(webpage)

############################################################################
##import requests 
from bs4 import BeautifulSoup 
soup = BeautifulSoup( web_byte,'html.parser')
for a in soup('a'):
    a.decompose()
for a in soup('br'):
    a.decompose()
for a in soup('span'):
    a.decompose()
for a in soup('strong'):
    a.decompose()
for a in soup('head'):
    a.decompose()
for a in soup('button'):
    a.decompose()
text = soup.find_all('p',limit=10)
print(text)
#############################################################################
#print(soup.get_text(''))
##soup.get_text(' ',strip=True)
##soup.body.p.next.next.string.strip()
##soup.html.body.nextSibling
##soup.find_all('p').string
##soup.find_all('p').name
##soup.find_all(['a','p']).string  returns a and b both tag
#print(soup.find_all(True))  #returns tag name
##soup.find_all(class_and_id)
##soup.findChildren('table','results')
##movie[0].find('a').contents[0]
##movie[0].find('span','genre').find_all('a')











