import os, sys
import pyttsx
from Speech import *

voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', '80')
voiceEngine.say('You can check the full source code bellow, where we will iterate through multiple voice speech ratings and volumes. Note that we are increasing the speech rate by 50 words per minute in each iteration (starting by 50) until 300 words per minute. Then, we maintaint the speech rate at 125 words per minute and iterate the volume from 0.1 to 1, increasing 0.3 in each iteration. Also, don’t forget to call the runAndWait method in the end of each iteration, so the voice is synthesized.')
voiceEngine.runAndWait()