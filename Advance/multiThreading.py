
from threading import *
import time

class Hello(Thread):
    def run(self):
        for _ in range(5):
            print('hello')
            time.sleep(1)


class Hi(Thread):
    def run(self):
        for _ in range(5):
            print('hi')
            time.sleep(1)


t1 = Hello()
t2 = Hi()


# t1.run()
# t2.run()

t1.start()  # internally it will call run method, because there is a inbuild method called run
t2.start()  # internally it will call run method

t1.join()
t2.join()   # main thread will wait for execution of t2 thread then it will execute

print("Byee")