#Import Libraries
import speech_recognition as sr
import datetime
r=sr.Recognizer()
def googlelisten():
    #Get the default microphone
    with sr.Microphone() as source:
        audio=r.listen(source)

        command=r.recognize_google(audio)
        return command

        #Listens to command,using
while True:
    command=googlelisten()
    print(command)
    break





