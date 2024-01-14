import speech_recognition as sr
import pyttsx3



def speak(audio):
    
    #  ENGINE  #
    engine = pyttsx3.init()

    #  VOICES  #
    voices = engine.getProperty("voices")

    #  CHOOSE VOICE  #
    engine.setProperty("voice", voices[1].id) 

    #  SPEED OF SPEECH  #
    engine.setProperty("rate", 130)

    #  SPEECH  #
    engine.say(audio)

    #  END  #
    engine.runAndWait() 



speak("Hello")
#  LISTEN  #

def listen():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
    
    except Exception as e:

        print(e)
        return "---"
    
    return query



#  CICLE  #

if __name__ == "__main__":
    
    while True:
        
        query = listen().lower()
        print(query)


