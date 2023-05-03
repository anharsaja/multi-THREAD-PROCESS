from threading import Thread
from time import sleep
import keyboard
import os

os.system('cls' if os.name == 'nt' else 'clear')

i = 0
def f1():
    global i
    while i <= 10:
        print(i, 'T1')
        i += 1
        sleep(0.75)

def f2():
    global i
    while True:
        if keyboard.is_pressed('space'):
            i = 10
            break

t2 = Thread(target=f2)

t2.start()
f1()

# Thread Ended All Process
# Normal Process is Ended by Thread

# BOT = Normal process
# Runner = Executor