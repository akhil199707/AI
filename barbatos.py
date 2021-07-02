import pyttsx3                 # text to speech package need to install
import datetime                # date and time package
import speech_recognition as sr # speech recognition package need to install
import wikipedia                # wikipedia for definitions need to install
import smtplib                  # used to send mail (SMTP/ESMTP)
import webbrowser as wb         # web browser package
import psutil                   # to know about cpu and battery need to install
import pyjokes                  # tells jokes need to install
import os                        # used to do operating system comands
import pyautogui                 # package used for automate the mouse and keyboard need to install
import json                            # convert python to json and vice versa
import requests                         # elegant HTTP library
from urllib.request import urlopen       # module for fetching URLs
import wolframalpha                      # used as calculator need to install
import time as t                           # to stop listening
import geocoder                              # current user location
import clipboard                               # used for reading text
import string                                  # password generation
import random                                  # password generation
from newsapi import NewsApiClient


engine = pyttsx3.init()        #initializing text to speech function
#engine.setProperty("rate", 180)#speed of speech
wolframalpha_app_id = 'HGWW2W-AQT3TG5HQE'



def speak(audio):               #audio function
    engine.say(audio)
    engine.runAndWait()

def time():                      #time function
    Time = datetime.datetime.now().strftime("%I:%M%p")
    speak(Time)

def date():                       #date function
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def greating():                    #greating function
    speak("barbatos lupus rex online")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour<= 24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir!")
    speak("barbatos at your command sir")


def takecommand():                                #accepting commands using speech recognition and its function
    r = sr.Recognizer()                               #used to Recognize my voice
    with sr.Microphone() as source:                  #activate mic
        print("listening.....")
        r.pause_threshold = 1                          #time to wait for user commands
        audio = r.listen(source)                       #whatever it listens its stored in source

    try:                                                     #error handling
        print("Recognizning....")
        query = r.recognize_google(audio, language='en-in')        #stores the value of user command recognized by google
        print(query)

    except Exception as e:                                   #error to handle
        print(e)
        speak("can't get what you said sir....")
        return "None"
    return query

def  sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)           #server to send mail and its port
    server.ehlo()
    server.starttls()                                      #for this function, you must enable low security in your gmail which you are going to use as sender
    server.login('codelabsdevloper@gmail.com','Alpha@01')           #login to gmail
    server.sendmail('codelabsdevloper@gmail.com',to,content)        #https://www.google.com/settings/security/lesssecureapps use this link to send email
    server.close()

def cpu():                                                     # cpu and battery details
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    speak("%")

def joke():                                # jokes function
    speak(pyjokes.get_joke())

def screenshot():                               # screenshot function
    img = pyautogui.screenshot()
    img.save('my_screenshot.png')

def text2speech():                               # selected text read function
    text = clipboard.paste()
    print(text)
    speak(text)

def passwordgen():                               # password generation function
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak("Sir! your password is made")

def news():
    newsapi = NewsApiClient(api_key='b07b90f8d9f24ab59f0efa2f69a76669')
    speak("On what would you like to know Sir....")
    topic = takecommand().lower()
    data = newsapi.get_top_headlines(q=topic,language='en',page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("these are all the news about "+topic)


if __name__ == '__main__':              #main function

    greating()

    while True:
        query = takecommand().lower()   # all commands will be stored in lower case in query for easy recognition

        if 'time' in query:
            time()
            speak("Sir")

        if 'date' in query:
            date()
            speak("Sir")

        elif 'wikipedia' in query:       #search in wikipedia
            speak("Searching Sir......")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                #provider reciver email address
                speak("To whom should I send the mail sir?")
                reciever=input("Enter email:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:                                   #error to handle
                print(e)
                speak("can't send email")

        elif 'search web' in query:
            speak("What should i search sir?")
            bravepath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            #bravepath is location of brave's installation on computer

            search = takecommand().lower()
            wb.get(bravepath).open_new_tab(search+'.com')     #only works with websits that end with .com

        elif 'search in youtube' in query:                     # Search in youtube
            speak("what do you want to see sir?")
            search_Term = takecommand().lower()
            speak("here are your results sir...")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search' in query:                          # search in google
            speak("what would you like to know sir?")
            search_Term = takecommand().lower()
            speak("here are your results sir...")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:                       # cpu and battery details
            cpu()

        elif 'joke' in query:                     # jokes
            joke()

        elif 'offline' in query:                    # offline
            speak('OFFLINE MODE')
            quit()

        elif 'open word' in query:                  #open word
            speak('opening sir')
            path = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(path)

        elif 'note' in query:                 # write notes
            speak('what to write, Sir?')
            notes = takecommand()
            file = open('notes.txt','w')
            speak('should i include date and time?')
            ans = takecommand().lower()
            if 'yes' or 'sure' in ans:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(':-')
                file.write(notes)
                speak('Done with notes, SIR!')
                file.close()
            else:
                file.write(notes)
                speak('Done with notes, SIR!')
                file.close()

        elif 'open notes' in query:                      # open notes
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
            file.close()

        elif 'screenshot' in query:                     # take screenshot
            screenshot()
            speak('took the screenshot')

        elif 'songs' in query:                            #songs from spotify
            speak("what would you like to listen sir?")
            search_Term = takecommand().lower()
            speak("here are your results sir...")
            wb.open('https://open.spotify.com/search/'+search_Term)

        elif 'remember that' in query:                  # reminder
            speak('what should I note down sir?')
            memory = takecommand().lower()
            speak('Sir you have asked me to remember that '+memory)
            reminder = open('memory.txt','w')
            reminder.write(memory)
            reminder.close()

        elif 'do you remember anything' in query:               # checking in reminder
            speak('please wait sir')
            file = open('memory.txt','r')
            print(file.read())
            speak(file.read())
            file.close()

        elif 'news' in query:                                     # news
            news()

        elif 'where is' in query:                                          # location
            query = query.replace("where is","")
            location = query
            speak("Sir you would like to know"+location)
            wb.open('https://www.google.co.in/maps/place/'+location)

        elif 'calculate' in query:                                       # calculator
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is:'+answer)
            speak('The answer is'+answer)

        elif 'what is' in query or 'who is' in query:                     # answers to questions
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print('No results')
                speak("can't find anything Sir...!")

        elif 'pause' in query:                                       # pause listening
            speak('For how many seconds should I be offline ?')
            ans = int(takecommand())
            t.sleep(ans)
            print(ans)

        elif 'log out' in query:                              # system log off
            os.system("shutdown -l")
        elif 'restart' in query:                              # system restart
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:                             # system shutdown
            os.system("shutdown /s /t 1")

        elif 'weather' in query:                                     # weather details
            current_location = geocoder.ip('me')
            place = current_location.city
            print(place)
            url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid=85a23ecf2212f4cbf9771c074aa89306'
            res = requests.get(url)
            data = res.json()
            weather = data['weather'] [0] ['main']
            temp = round((data['main']['temp']-32)*5/9)
            desp = data['weather'][0]['description']
            print(weather)
            print(temp)
            print(desp)
            speak(f'Weather in {place} is')
            speak('Temperature : {} degree celcius'.format(temp))
            speak('Weather : {}'.format(desp))

        elif 'read' in query:                       # read the selected text
            text2speech()

        elif 'new password' in query:               # password generation
            passwordgen()
