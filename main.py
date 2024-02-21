import pyttsx3
import os
import speech_recognition as sr
import speech_recognition as sr 
import webbrowser
import wikipedia
import pyaudio
import datetime
import config
# import threading
from gemini import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)    
    if hour >=0 and hour <4 or \
       hour>=19 and hour <24:
        speak('Good night sir!,')
    elif hour>=4 and hour<12:
        speak('Good Morning sir! ,')
    elif hour>= 12 and hour <16:
        speak('Good  Aafternoon  sirr!,')    
    else :
        speak('Good Evening!')    
    speak('I  am  Jarvis , how  may  I  help  youu  sirr!')  
   
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
    
    except Exception as e:
        print(e)
        return ''
    return query

# t1=threading.Thread(target=take_command())
# t2=threading.Thread(target=query)

# t1.start()
# t2.start()
# print(query)
wishMe()
# click_on_chat_button() 
def AI():
    sendQuery(query)
    isBubbleLoaderVisible()
    response = retriveData()
    speak(response)

while True:

    query= take_command().lower()

    print('\n You: '+ query)

    #logic to excuteing task based on query
    if 'wikipedia' in query:
        speak('searching wikipedia......')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=3)
        speak('According to wikipedia.....')
        print(results)
        speak(results)

    if 'open youtube' in query:
        speak('opening youtube.')
        webbrowser.open('youtube.com') #website url.

    elif 'open google' in query:
        speak('opening google.')
        webbrowser.open('google.com')

    elif 'open chat GPT' in query:
        speak('opening Chat G P T.')
        webbrowser.open('chat.openai.com')

    elif 'open instagram' in query:
        speak('opening instagram.')
        webbrowser.open('instagram.com')

    elif 'open temp mail' in query:
        speak('opening temp mail.')
        webbrowser.open('temp-mail.org')

    elif 'open mail' in query:
        speak('opening gmail.')
        webbrowser.open('mail.google.com') 

    elif 'play music' in query:
        speak('playing music.')
        music_dir = 'C:\\Users\\Shubham Manoj Gupta\\Music\\fav song' #location of music folder
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'open vs code' in query:
        speak('opening Visual studio Code.')
        code = "C:\\Users\\sss\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  #target location of .exe file
        os.startfile(code)

    elif 'open browser' in query:
        speak('opening brave browser.')
        browser = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  #trace location of .exe file
        os.startfile(browser)

    elif 'open telegram' in query:
        speak('opening telegram')
        Tg = "C:\\Users\\sss\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe" #trace location of .exe file
        os.startfile(Tg)

    elif 'time' in query:
        strTime  = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sir,the time is {strTime}')
        print(strTime)

    elif 'shutdown' in query:
        speak('shutting down your pc ',os.system('shutdown /s /t 1'))   

    elif 'restart PC' in query:
        speak('restarting your pc', os.system('shutdown /r /t 1'))

    elif 'search on' in query:
        srch=take_command()
        srch=srch.replace('search on browser for','')
        speak(f'searching for {srch} on browser')
        brow="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
        webbrowser.get(brow).open_new_tab(srch)

    
    elif 'Jarvis quit' in query:
        speak('terminating this session, have a nice day sirr!')
        exit()    

    # else:
    #     chat=chat1(query)
    #     chat.replace('*','')
    #     print(chat)
    #     speak(chat)
    else: 
        
        chat=chat1(query)
        print('\n JARVIS:- '+ chat)
        speak(chat)
