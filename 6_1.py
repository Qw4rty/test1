# 1zadanie posledovatelno
from threading import Thread
import time
from datetime import datetime

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)
t1 = datetime.now()
for i in range(5):
    get_thread(i + 1)
print('time ', (datetime.now() - t1).microseconds)