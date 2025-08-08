import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from dotenv import load_dotenv
load_dotenv()


recognizer=sr.Recognizer()
NEWS_API_KEY=os.getenv("NEWS_API_KEY")

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def get_news_titles():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            return ["Failed to fetch news."]

        # Get top 5 headlines
        titles = [article["title"] for article in data["articles"][:5]]
        return titles
    except Exception as e:
        return [f"Error fetching news: {e}"]


def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        headlines=get_news_titles()
        for title in headlines:
            speak(title)
        speak("News Ended!")
        
    

if __name__=="__main__":
    speak("Initializing Jarvis....")
    
    while True:
        r=sr.Recognizer()
                  
        try:
            #listen for wakeup Word
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source)
            
            print("Recognizing...")
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Ya, I am Listening...")
                
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    
                    process_command(command)
             
        except Exception as e:
            print(f"Error; {e}")