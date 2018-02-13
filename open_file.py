import Windows_search
import os
from Windows_search import winsearch
def open(string):
    path = winsearch(string)
    if not path =="":
        #os.system("start string")
        os.startfile(path)