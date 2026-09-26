import time
import threading

def function1():
    print("this is function1")
    time.sleep(5)
    print('after 5 sec function end')

def function2():
    print('this is function2')

timerThread = threading.Thread(target=function1)
# This is function call
timerThread.start()

function2()

'''
this is function1
this is function2
after 5 sec function end --> this will print after 5 second, we can run concurrent function at a time
'''