from subprocess import getoutput
from threading import Thread
from timeit import *
from time import *
from random import *


# commandexec = lambda cmd: list(filter(lambda x: True if x != '' else False, getoutput(cmd).split("\n")))

# class Excecutor:
#     activating = commandexec('cscript //nologo c:\windows\system32\slmgr.vbs /ato')

import threading
import time

class Demo:
    def __init__(self):
        self._KillTask = False
        self.sleepTime = 0
        self.counter = 0
        self.randomint = randint(5, 10)
        self.statement = False

    def OnTimeout(self):
        self._KillTask = True
        print("Timeout!")
    
    def Counter(self):
        print("Counter() starts! end at", self.randomint)
        while(self._KillTask is False):
            print(self.counter)
            self.counter += 1
            print(f"Waiting {self.counter}s")
            time.sleep(0.75)
            if self.counter == self.randomint:
                self.OnTimeout()
            
    
    def Function(self):
        while self._KillTask is False:
            #do any logic here
            # print(f"[{self.sleepTime}] Function is running till it timeout..")
            self.sleepTime += 1
            time.sleep(0.75) #  just a demo delay for the printed log on the terminal
            if self.sleepTime == 9:
                self.statement = True
                break
        # print("Function() timed out!")
        self._KillTask = True


if __name__=='__main__':
    ## Main starts here
    print("Demo for Timeout - by Omar")
    Obj = Demo()
    
    ## Start thread2 
    thread2 = threading.Thread(target = Obj.Counter)
    try:
        thread2.start()
    except Exception:
        print ("Error Starting the Thread")
    
    ## Proceed with the logic of thread 1 -(Main thread)
    Obj.Function()
    print(Obj.statement)