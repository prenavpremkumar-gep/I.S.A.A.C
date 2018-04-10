import win32api
import os
import sys
import glob
import re
import io
from Speech import chat_speak
found = 0
'''chat_speak("Enter a keyword to search in filename")
file_name = input('Enter a keyword to search in filename: ')'''
matches = []

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
#print(drives)

def read_file(file_name):
    with io.open('file_list.txt', 'r', encoding="utf-8") as f:
        user_list = [line.rstrip('\n') for line in f]
        for i, x in enumerate(user_list):
            # regex = re.findall(r"(?i)(.*)file(.*)",x)
            if file_name in x:
                matches.append(x)
    for i, x in enumerate(matches):
        print(i + 1)
        print(x)
    chat_speak("Your choice")
    file_choice = int(input("Enter your choice: "))
    os.startfile(matches[(file_choice - 1)])
    f.close()


def write_file():
    with io.open('file_list.txt', 'w',encoding="utf-8") as fp:
        for d in drives:
            for dirname, dirnames, filenames in os.walk(d):
                for file in filenames:
                    act_path = os.path.join(dirname, file)
                    act_path = os.path.abspath(act_path)
                    print(act_path)
                    fp.write(act_path + '\n')
    fp.close()

def keyword_search():
    chat_speak("Enter a keyword to search in filename")
    file_name = input('Enter a keyword to search in filename: ')
    try:
        read_file(file_name)
    except IOError:
        write_file()
        read_file(file_name)
