import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")  
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]     
        webbrowser.open(link) 

if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
        r = sr.Recognizer()
        print("recognizing...")        
        try:
            with sr.Microphone() as source:
                print("listning")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)            
            word = r.recognize_google(audio)
            print(f"Recognized word: {word}") 
            if(word.lower()=="jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)   
                    command = r.recognize_google(audio)   
                    print(f"Command: {command}")  
                    
                    processCommand(command)                
                
        except Exception as e:
            print(f"Error: {e}")