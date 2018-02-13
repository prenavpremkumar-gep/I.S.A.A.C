'''
This code is for the first start of the day. Intialises the system, checks for updates,looks for mails, notifications.
Also checks reminders and alarms or whatever is added for initial user needs.
'''
import os
import time, sys
import warnings
import aiml
from Audio import *
import ISAAC


mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sroe
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature.\nStarting text mode\n")

terminate = ['bye','buy','exit','quit','gotosleep','goodbye']

while True:
    if mode == "voice":
        response = listen()
        print(response)
    else:
        username=os.getlogin()
        response = input(username+": ")
    if response.lower().replace(" ","") in terminate:
        break

    ISAAC.isaac(response)
