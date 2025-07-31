import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    

if __name__=="__main__":
    speak("Initializing Jarvis....")
    
    while True:
        r=sr.Recognizer()
                  
        try:
            #listen for wakeup Word
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            
            print("Recognizing...")
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Ya, I am Listening...")
                
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)
                    
                    process_command(command)
             
        except Exception as e:
            print(f"Error; {e}")