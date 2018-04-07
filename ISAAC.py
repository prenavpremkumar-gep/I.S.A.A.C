'''
this is the processigng hub and center of all actions of the VA.
all commands and actions are imported and processed here.
'''
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from open_file import open
import os
import aiml
import web_browse
from search import websearch
from power import *
from Windows_search import winsearch
from Speech import speak
from Speech import chat_speak
from sending_email import send_initiate
from reading_email import reading
from keyword_file_search import keyword_search

def isaac(string):
    '''
Defines the whole working scheme of ISAAC
    '''
    case = 0
    kernel = aiml.Kernel()
    unfiltered = string
    string = string.lower()
    #print(string)
    u = ["you", "your"]
    signoff = ["logout","logoff", "signout"]
    word_list = word_tokenize(string)
    #pos_list = nltk.pos_tag(word_list)
    stop_words= set(stopwords.words('english'))
    if "search" not in word_list and "google" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
        filtered_sentence = [w for w in word_list]
    #print(filtered_sentence)
    if 'open' in filtered_sentence:
        # Opening a file
       if 'file' in filtered_sentence and \
             filtered_sentence.index('open') \
             < filtered_sentence.index('file'):
           if "called" in string:
               pos = unfiltered.index("called") + 7
               unfiltered = unfiltered[pos:]
           elif "named" in string:
               pos = unfiltered.index("named") + 6
               unfiltered = unfiltered[pos:]
           else:
               pos = unfiltered.index("file") + 5
               unfiltered = unfiltered[pos:]
           case = 1
           speak(case)
           open(unfiltered)


    #Opening an application

    #Browsing the web

       elif 'site' in filtered_sentence:
            filtered_sentence = [w for w in filtered_sentence \
                                 if w != "called" and w != "named"]
            case = 1
            speak(case)
            web_browse.browse( \
                filtered_sentence[filtered_sentence.index('site') + 1])
       elif 'website' in filtered_sentence and \
                       filtered_sentence.index('open') \
                       < filtered_sentence.index('website'):
           case = 1
           speak(case)
           web_browse.browse( \
               filtered_sentence[filtered_sentence.index('website') + 1])
    #Searching(Query)
    if word_list[0] in ["who", "when", "where", "how","what"] :
        if not("you" in word_list or "your" in word_list):
            websearch(string)
        else:
            if os.path.isfile("bot_brain.brn"):
                kernel.bootstrap(brainFile="bot_brain.brn")
            else:
                kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
            #print(string)
            answer = kernel.respond(string)
            print("ISAAC: "+answer)
            chat_speak(answer)

    #Searching(System)
    if 'search' in filtered_sentence and 'for' in filtered_sentence:
        if 'file' in filtered_sentence and \
                        filtered_sentence.index('search') \
                        < filtered_sentence.index('file'):
            pos = unfiltered.index("file") + 5
            unfiltered = unfiltered[pos:]
        else:
            pos = unfiltered.index("for") + 4
            unfiltered = unfiltered[pos:]
        case = 2
        speak(case)
        keyword_search()
        #winsearch(unfiltered)

    #Playing Music in native app

    #Shutdown options

    elif "shutdown" in filtered_sentence:
        print("Are you sure?")
        chat_speak("Are you sure?")
        resp = input()
        if resp == "yes":
            chat_speak("Shutting down")
            shutdown()
    elif "restart" in filtered_sentence:
        print("Are you sure?")
        chat_speak("Are you sure?")
        resp = input()
        if resp == "yes":
            chat_speak("Rebooting in 60 seconds")
            restart()
    for s in signoff:
        if s in filtered_sentence :
            print("Are you sure?")
            chat_speak("Are you sure?")
            resp = input()
            if resp == "yes":
                chat_speak("Logging off in 60 seconds")
                logout()
    if "abort" in string:
        abort_shutdown()
    #Send Mail
     if 'send' in filtered_sentence :
        send_initiate()
    #Checking Mail
     if 'read' in filtered_sentence and 'mail' in filtered_sentence:
        reading()
     #Alarm
    #Setting a reminder
    #System Update

    return ""
