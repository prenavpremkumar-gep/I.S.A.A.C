#https://www.chatbots.org/ai_zone/viewthread/1799/ - how to execute
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

terminate = ['bye','buy','shutdown','exit','quit','gotosleep','goodbye']
#Add code for text or voice input
def offline_speak(jarvis_speech):
	#Write code here

def listen():
	#Write code here
kernel = aiml.Kernel()
'''
If a brainFile argument is provided, the Kernel attempts to
load the brain at the specified filename.

If learnFiles is provided, the Kernel attempts to load the
specified AIML files.

Finally, each of the input strings in the commands list is
passed to respond().
'''
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
	#kernel.saveBrain("bot_brain.brn")
	'''
	When you start to have a lot of AIML files, it can take a long time to learn. 
	This is where brain files come in. After the bot learns all the AIML files it can 
	save its brain directly to a file which will drastically speed up load times on subsequent runs.
	'''
# Create the kernel and learn AIML files PyAIML
'''
Load and learn the contents of the specified AIML file.

If filename includes wildcard characters, all matching files
will be loaded and learned.
'''
#kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")
#kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    if mode == "voice":
        response = listen()
    else:
        response = raw_input("Talk to ISSAC : ")
    if response.lower().replace(" ","") in terminate:
		break
		'''while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response'''
    issac_speech = kernel.respond(response)
    print "ISSAC: " + issac_speech
    offline_speak(issac_speech)
    
