import speech_recognition as sr




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


