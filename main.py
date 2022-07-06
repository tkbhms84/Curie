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

def getdate():
    return datetime.datetime.now().strftime('%I:%M %p')
while True:
    command=googlelisten()
    print(command)
    if 'time' in command:
        print(getdate())
    break





