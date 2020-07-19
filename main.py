import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
import time
import random
import pyautogui
from pygame import mixer
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# songs
randomfile = random.choice(os.listdir("D:\\Python Projects\\jaadu\\Songs\\"))
file = r'D:\\Python Projects\\jaadu\\Songs\\' + randomfile


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 4:
        speak("Good Night")

    elif hour >= 4 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("Hello, I am Jaadoo !!")
    speak("Now, what can i do for you??")


def takeCommand():
    # It takes microphone input from the user and returns string output

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
        return "None"
    return query


def song(file):

    print(file)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    return


def pause(file):
    mixer.music.pause()
    return


def resume(file):
    mixer.music.unpause()
    return


def Whatsapp(contact, message, media, answer):
    driver = webdriver.Chrome(
        "C:\\selenium driver\\geckodriver.exe")
    driver.get("https://web.whatsapp.com")
    time.sleep(5)
    driver.find_element_by_css_selector(
        "body.web:nth-child(2) div._347-w._2UMYL.app-wrapper-web.font-fix div.app.h70RQ.two:nth-child(6) div._1-iDe._1xXdX:nth-child(3) div._1FTCC div.rRAIq div.gQzdc label._2MSJr:nth-child(4) div._3F6QL._3xlwb > div._2S1VP.copyable-text.selectable-text").send_keys(contact)
    pyautogui.press('enter')
    if (answer == "text"):
        driver.find_element_by_css_selector(
            "body.web:nth-child(2) div._347-w._2UMYL.app-wrapper-web.font-fix div.app.h70RQ.two:nth-child(6) div._1-iDe.Wu52Z:nth-child(4) div._1GX8_ footer._2tW_W:nth-child(7) div._3pkkz.V42si.copyable-area div._1Plpp:nth-child(2) div._3F6QL._2WovP > div._2S1VP.copyable-text.selectable-text").send_keys(message)
        time.sleep(2)
        pyautogui.press('enter')

    else:
        print("Hello World!!")

    # elif (answer == "media"):
    #     driver.find_element_by_xpath('')


def Youtube(search):
    driver = webdriver.Chrome(
        "C:\\selenium driver\\geckodriver.exe")
    driver.get("https://www.youtube.com")
    driver.find_element_by_xpath("//input[@id='search']").send_keys(search)
    driver.find_element_by_xpath(
        "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']").click()
    time.sleep(2)
    driver.find_element_by_class_name("style-scope ytd-video-renderer").click()


def Google(search):
    driver = webdriver.Chrome(
        "C:\\selenium driver\\geckodriver.exe")
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='q']").send_keys(search)
    pyautogui.press('enter')
    time.sleep(2)
    driver.find_element_by_class_name("r").click()


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def News():
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=2b646a5171fb41e9816f33fb8d4ad55e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next News")
    speak("Thanks for listening...")


if __name__ == "__main__":
    wishMe()
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

        elif 'youtube' in query:
            speak("Opening Youtube !!")
            speak("What to Search !!")
            search = takeCommand()
            Youtube(search)

        elif 'google' in query:
            speak("Opening google")
            speak("what to search?")
            search = takeCommand()
            print(search)
            Google(search)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Playing music!!")
            speak("Get Ready to Rock!!")
            song(file)

        elif 'pause' in query:
            pause(file)

        elif 'resume' in query:
            resume(file)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'whatsapp' in query:
            try:
                speak("To whom i have to send??")
                contact = takeCommand()
                print(contact)
                speak("Text or Media?")
                answer = takeCommand()
                if 'text' in query:
                    speak("What to send??")
                    message = takeCommand()
                    print(message)

                elif 'media' in query:
                    speak("I will pick that from contact location..")

                Whatsapp(contact, message, media, answer)

            except Exception as e:
                print(e)

        elif 'what are today headlines' in query:
            speak('Todays news are..')
            News()
