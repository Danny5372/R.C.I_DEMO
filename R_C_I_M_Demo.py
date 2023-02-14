import time
import subprocess 
import keyboard as key 
from fbchat import Client
from fbchat.models import *
#VERSION
version = "demo 1.0"
#INSTALLATION
""""
pip install fbchat
pip install keyboard
"""
#LOGIN SEQUENCE - MUST BE FRIEND WITH THE PROGRAM BEFORE STARTING
client = Client('<Your fake account email>', '<Your fake account password>')
users = client.searchForUsers('<Your facebook account name>')
user = users[0]
#TARGETED SENDER - USE THE MAIN ACCOUNT TO TEXT AND CONTROL
print("User's ID: {}".format(user.uid)) #Recieve your ID here
print("User's name: {}".format(user.name))
print("User's profile picture URL: {}".format(user.photo))
print("User's main URL: {}".format(user.url))

def message_check():  
    global command
    time.sleep(5)
    messages = client.fetchThreadMessages(thread_id="<Your facebook ID>", limit=1)
    for message in messages:
        command = message.text
        print(message.text)

while True:
    message_check()
    action = command.split()

    #OPEN COMMAND: open [browser] [key words/links]
    if "open" in command:
        client.send(Message(text="Opening"), thread_id=user.uid, thread_type=ThreadType.USER)
        time.sleep(0.5)
        if 'chrome' in command:
            subprocess.call("C://Program Files/Google/Chrome/Application/chrome.exe") #If it fails, redirect directory.
            client.send(Message(text="Opened"), thread_id=user.uid, thread_type=ThreadType.USER)
            if len(action) >= 3:
                client.send(Message(text="Entering key words/links"), thread_id=user.uid, thread_type=ThreadType.USER)
                time.sleep(0.5)
                key.write(action[2])
                time.sleep(0.5)
                key.press('enter')
                client.send(Message(text="Done"), thread_id=user.uid, thread_type=ThreadType.USER)
    #TYPE COMMAND: type [str1] [str2] [str...]
    if 'type' in command:
            client.send(Message(text="Typing"), thread_id=user.uid, thread_type=ThreadType.USER)
            if len(action) >= 1:
                time.sleep(2)
                print(len(action))
                for i in range(len(action)):
                    if i == i and i < len(action)-1:
                        print(i)
                        i += 1
                        key.press('space')
                        key.write(action[i], 0.1)
                        i -= 1
            client.send(Message(text="Done"), thread_id=user.uid, thread_type=ThreadType.USER)

    #PRESS COMMAND: press [key1] [key2]
    if "press" in command:
        time.sleep(2)
        key.press(action[1])
        print(len(action))
        client.send(Message(text="Pressing"), thread_id=user.uid, thread_type=ThreadType.USER)
        if len(action) == 3:
            key.press_and_release(f"{action[1]} + {action[2]}")
        elif len(action) >= 4:
            client.send(Message(text="More than limit, exacution failed"), thread_id=user.uid, thread_type=ThreadType.USER)
        client.send(Message(text="Done"), thread_id=user.uid, thread_type=ThreadType.USER)

    #EXIT COMMAND: exit
    if "exit" in command:
        client.send(Message(text="Exiting"), thread_id=user.uid, thread_type=ThreadType.USER)
        time.sleep(10)
        client.send(Message(text="Done"), thread_id=user.uid, thread_type=ThreadType.USER)
        break
    else:
        print("No command received")
