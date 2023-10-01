# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:00:55 2022

@author: RUTURAJ PATIL
"""

from unittest import result
from zipfile import Path
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
voicespeed = 160
engine.setProperty('rate', voicespeed)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good moorning")
    elif hour >= 12 and hour < 17:
        speak("good afternoon")
    elif hour >= 17 and hour < 19:
        speak("good Evening")
    else:
        speak("good night")

    speak("Stuert is online. How Can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
        speak(f"you said:{query}\n")


    except Exception as e:
        print(e)
        print("say that again please sir......")
        return "none"

    return query

chatgpt_url = 'https://chat.openai.com/'
chrome_binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

chrome_options = Options()
chrome_options.binary_location = chrome_binary_location
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open translator' in query:
            webbrowser.open("https://translate.google.com/?sl=en&tl=mr&op=translate")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open patil' in query:
            Path = "E:\\"
            os.startfile(Path)

        elif 'search' in query:
            speak('Searching....')
            query = query.replace("search", "")
            # result = webbrowser.open_new_tab(query)
            # result = webbrowser.get('chrome').open_new_tab(query)
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.get('chrome').open_new_tab(search_url)

            speak("there is some results")

        # elif 'open wamp' in query:
        #     Path = "C:\\wamp\\wampmanager.exe"
        #     os.startfile(Path)

        elif 'open vscode' in query:
            Path = "C:\\Users\\Ruturaj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        # elif 'question' in query:
        #     speak('Opening ChatGPT...')
        #     chatgpt_url = 'https://chat.openai.com/'  # Replace with the actual URL of ChatGPT
        #     chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        #     driver = webdriver.Chrome(chrome_path)
        #     driver.get(chatgpt_url)
        #     chat_input = driver.find_element_by_xpath('//input[@id="chat-input"]')
        #     chat_input.send_keys(query)
        #     chat_input.send_keys(Keys.RETURN)
        #     speak("Opening ChatGPT with the query.")

        elif 'question' in query:
            speak('Opening ChatGPT...')
            query = query.replace('question is', '').strip()
            encoded_query = urllib.parse.quote(query)
            search_url = f'{chatgpt_url}?query={encoded_query}'

            webbrowser.get().open_new_tab(search_url)
            time.sleep(5)  # Wait for the chat page to load

            # Simulate keyboard input to enter the query
            pyautogui.typewrite(query)
            pyautogui.press('enter')

            speak("Opening ChatGPT with the query.")



        elif 'exit' in query:
            speak('Goodbye!')
            break





