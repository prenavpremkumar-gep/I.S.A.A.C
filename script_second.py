# https://www.chatbots.org/ai_zone/viewthread/1799/ - how to execute
import aiml
import os
import sys
import warnings

mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature.\nStarting text mode\n")

terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
# Add code for text or voice input
# def offline_speak(jarvis_speech):
# Write code here
# def listen():
# Write code here
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
# kernel.saveBrain("bot_brain.brn")
# Create the kernel and learn AIML files PyAIML
# kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    if mode == "voice":
        response = listen()
    else:
        response = input("Talk to ISSAC : ")
    if response.lower().replace(" ","") in terminate:
        break
    # kernel.saveBrain("bot_brain.brn")
    print(response)
    issac_speech = kernel.respond(response)
    print("ISSAC: " + issac_speech)
    # offline_speak(issac_speech)
