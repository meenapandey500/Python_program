import threading

def task():
    print("timer object task running...")

if __name__=='__main__':
    t = threading.Timer(10, task)
    t.start() # after 10 seconds, task will be executed
