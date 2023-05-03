from threading import Thread
from time import sleep
from subprocess import getoutput
from timeit import timeit
from random import randint
import os

os.system("cls" if os.name == "nt" else "clear")

# main properties:
# command to execute and the result

class RandomTimeout:
    def __init__(self, message, threadout, sleeptime) -> None:
        self._endTask = False
        self.message = message
        self.timeoutsec = threadout+1 # 1m 30s
        self.result = None
        self.sleeptime = sleeptime
        self.typetime = None

        self.timeout = Thread(target=self.Timeout, args=(0,))
        try:
            self.timeout.start()
            self.Execution()
        except Exception as e:
            self._endTask = True
            self.timeoutsec = 0
            print(self.timeoutsec)
            print(e)
        
    def Execution(self):
        print(self.message)
        while self._endTask == False:
            x, y = randint(0, 5), randint(0, 5)
            sleep(self.sleeptime)
            if x == y:
                # self.result = f"Found! at sec-{self.timeoutsec}"
                self.result = f"On the {self.timeoutsec}sec => {x} {y} {self.typetime}"
                self._endTask = True
                self.timeoutsec = 0
        self._endTask = True

    def Timeout(self, sec):
        while self.timeoutsec > sec:
            if 10 < self.timeoutsec < 16:
                self.typetime = 1
                print(self.message, self.timeoutsec)
            elif self.timeoutsec <= 10:
                self.typetime = 2
                print(f"Timeout for the tasks {self.timeoutsec}s")
            self.timeoutsec -= 1
            if self._endTask == True:
                break
            sleep(self.sleeptime)
        else:
            self.result = "Timeout"
            self._endTask = True


    # def Animate(self):
    #     i = 0
    #     while 60 <= self.timeoutsec <= 100:
    #         print(f"{self.timeoutsec} {self.message} {'     '.replace(' ', '.', i)}")
    #         sleep(0.25)
    #         i += 1
    #         if i == 6:
    #             i = 0

y = RandomTimeout("Activating Windows", 15, 0.85)
print(y.result)

# i = 0
# message = 'Func'
# def func(): # stop
#     global i, message
#     while i < 20:
#         print(i, message)
#         sleep(0.85)
#         i += 1



# t1 = Thread(target=func)
# try:
#     t1.start()
# except KeyboardInterrupt:
#     i = 20







# i = 0
# j = 30
# while j > 0:
#     print(f"\r{j} Activating Windows {'       '.replace(' ', '.', i)}",end="")
#     sleep(0.25)
#     i += 1
#     if i == 6:
#         sleep(0.5)
#         i = 0
#         j -= 1


# end = 12
# start = 1
# i = 1
# while start <= end:
#     print(i*".")
#     i += 1
#     start += 1
#     if i == 4:
#         i = 1

# j = 1
# for i in range(50):
#     bracket = f"[{50*' '}]"
#     sleep(0.75)
#     print("Waiting", bracket.replace(' ', u'\u03BF', j))
#     j += 1
#     if j == 4:
#         j = 1

# for i in range(21):
#     bracket = f"[{20*' '}]"
#     print("\rWaiting", bracket.replace(' ', '=', i), end="")
#     sleep(0.05)


# bracket = "[   ]"
# print(bracket.replace(" ", "s", 3))

# def F1():
#     i = 0
#     j = 1
#     while j < 20:
#         print(f"\rActivating Windows{'       '.replace(' ', '.', i)}\n\rTimeout{j}",end="")
#         sleep(0.5)
#         i += 1
#         j += 1
#         if i == 6:
#             i = 0

# def F2():
#     for i in range(20):
#         print(f"\n\rTimeout {i}s",end="")
#         sleep(0.5)

# t1 = Thread(target=F1)
# t2 = Thread(target=F2)

# t1.start()
# print()
# class CommandTimeout:
#     def __init__(self, command, timeout) -> None:
#         self._endTask = False
#         self.command = command
#         self.timeoutsec = timeout+1 # 1m 30s
#         self.result = None

#         self.timeout = Thread(target=self.Timeout, args=(0,))
#         try:
#             self.timeout.start()
#         except Exception as e:
#             self._endTask = True
#             print(e)
#         self.Execution()

#     def Execution(self):
#         print(self.command)
#         while self._endTask == False:
#             cmdfilter = lambda cmd: list(filter(lambda x: True if x != '' else False, getoutput(cmd).split("\n")))
#             output = cmdfilter(self.command) # -> list
#             print(f"\rTimeout for the tasks {self.timeoutsec}s...",end="")
#             if len(output) > 0:
#                 self.result = output
#                 self._endTask = True
#             sleep(0.5) 
#         self._endTask = True

#     # override
#     def Timeout(self, sec):
#         while self.timeoutsec > sec:
#             self.timeoutsec -= 1
#             if self._endTask == True:
#                 print("Forcing to end Thread")
#                 break
#             sleep(0.5)
#         else:
#             print("\nTimeout")
#             self._endTask = True

    # def __repr__(self) -> str:
    #     return self.result

# class CommandTimeout:
#     def __init__(self, command, timeout) -> None:
#         self.command = command
#         self.timeout = timeout
#         self.result = None
#         self.end = False

#         self.waiter = Thread(target=self.Waiter, args=(self.timeout, ))
#         self.waiter.start()

#         self.Execution(self.command)

#     def Execution(self, command):
#         while self.end == False:
#             self.result = list(filter(lambda x: True if x != '' else False, getoutput(command).split("\n")))
#             if len(self.result) > 0:
#                 self.end = True

#     def Waiter(self, sec):
#         i = 0
#         while i < sec:
#             i += 1
#             sleep(1)
#             if self.end == True:
#                 break
#         else:
#             self.result = 'Timeout'

#     def __repr__(self) -> str:
#         return " ".join(self.result)

# print(CommandTimeout('cscript //nologo c:\windows\system32\slmgr.vbs /ipk DN6RP-97VRV-KRG6K-9P6MP-27JXG', 0.25))

# class CalledAsVar:
#     def __init__(self) -> None:
#         self.Printer()
    
#     def Printer(self):
#         print('Raden')

#     def __repr__(self) -> str:
#         return 'ToVar'

# x = CalledAsVar() # executes command
# print(x) # 


# THREAD FOR COUNTER
# CMD FOR EXEC


# class A(object):
#     def __new__(cls):
#         return [1,2,2]  
#     # It is not called
#     def __init__(self):
#         print("Init is called")
  
# print(A())

# def runafter5sec():
#     sleep(5)
#     print('Ran after 5 sec')

# t1 = Thread(target=runafter5sec)
# t1.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# class TimeoutCommand:
#     def __init__(self, cmd) -> None:
#         self.cmd = cmd
#         self.output = ""

#     def __str__(self):
#         return self.output

#     def Waiting(self):
#         t = Thread(target=self.)

#     def Executioner(self):
#         return list(filter(lambda x: True if x != '' else False, getoutput(self.cmd).split("\n")))

# commandexec('cscript //nologo c:\windows\system32\slmgr.vbs /ato')