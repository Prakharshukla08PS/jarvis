import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary 
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "feea4ddf3eef4cb58133671d81e32198"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def  processCommand(c):
     if "open google"in c.lower():
       webbrowser.open("https://google.com") 

     elif "open facebook"in c.lower():
       webbrowser.open("https://facebook.com") 

     elif "open youtube"in c.lower():
       webbrowser.open("https://youtube.com")   

     elif "open linkedin"in c.lower():
       webbrowser.open("https://linkedin.com")

     elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       linl = musiclibrary.music[song]
       webbrowser.open(linl)
         
     elif "news" in c.lower():   
       r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
       if r.status_code == 200:
         
            # Prase the Json response
            data = r.json()

            # Extract the article
            articles = data.get('articles',[])

            # Print the headline
            for article in articles:
              speak(article['title'])    

     else:
       #let OpenAi handle the request
       pass
        


if __name__ == "__main__":
    speak ("Initializing jarvis....")
    while True:
       #listen for the wake word "jarvis"
       # obtain audio from the microphone
       r = sr.Recognizer()
       with sr.Microphone() as source:
        print("listing...")
        audio = r.listen(source , timeout=2 , phrase_time_limit=2)

        print("recognizing...")    


       
       try:
        with sr.Microphone() as source:
         print("listing...")
         audio = r.listen(source , timeout=2 , phrase_time_limit=2)

        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
          speak("Ya")
          #listen for command
          with sr.Microphone() as source:
           print("Jarvis Active...")
           audio = r.listen(source)
           command = r.recognize_google(audio)

           processCommand(command)


       except Exception  as e:
        print("Error; {0}".format(e))