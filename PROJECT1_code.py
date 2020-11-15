# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:25:39 2020

@author: Akash
"""

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random 
import shutil 
import pyjokes 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Harrry Sir.") 

def usrname(): 
	speak("What should i call you sir") 
	uname = takeCommand() 
	speak("Welcome") 
	speak(uname) 
	columns = shutil.get_terminal_size().columns 
	
	print("#####################".center(columns)) 
	print("Welcome", uname.center(columns)) 
	print("#####################".center(columns)) 
	
	speak("How can i Help you, Sir")  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Can you repeat sir..")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akashvarde98@gmail.com', 'rtp$239HMr')
    server.sendmail('akashvarde98@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    clear = lambda: os.system('cls') 
    clear()
    wishMe()
    usrname()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music") 
            music_dir = 'F:\\Akash Varde  Memory Card all details\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            random = os.startfile(os.path.join(music_dir, songs[1]))
       
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "akashvarde98@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Akash and Rohan. I am not able to send this email") 
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        elif 'how are you' in query:
            speak('I am fine')
            speak('Ok Sir, have a good day.')
            
        elif 'fine' in query or "good" in query:
            speak('Its good to know that your fine')
            
        elif "what's your name" in query or "What is your name" in query:
            speak('My friends call me Harrrry..')
        
        elif "who made you" in query or "Who created you" in query:
            speak('I have been created by Akash and Rohan')
            
        elif "Joke" in query:
            speak(pyjokes.get_joke())
            
        elif "Power Point Presentation" in query:
            speak(pyjokes.get_joke())
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
        
        
            
            
            
        
            
         
            
        
            
            
            
            

       