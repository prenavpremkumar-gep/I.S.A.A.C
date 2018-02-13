import subprocess
import os

def shutdown():
    subprocess.call(["shutdown", "/s"])

def restart():
    os.system("shutdown /r")

def logout():
    os.system("shutdown /l")

def abort_shutdown():
    subprocess.call(["shutdown", "/a"])