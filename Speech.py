import pyttsx
import random


def speak(case):

    open = ["Opening ","Please wait", "Give me a minute"]
    search = ["Looking for it", "Searching the requested item"]

    if case==1:
        engine = pyttsx.init()
        rate = 150
        engine.setProperty('rate', rate)
        string = open[random.randint(0,2)]
        engine.say(string)
        engine.runAndWait()
    elif case ==2:
        engine = pyttsx.init()
        rate = 150
        engine.setProperty('rate', rate)
        string = search[random.randint(0, 1)]
        engine.say(string)
        engine.runAndWait()



def chat_speak(string):
    engine = pyttsx.init()
    rate = 150
    engine.setProperty('rate', rate)
    engine.say(string)
    engine.runAndWait()