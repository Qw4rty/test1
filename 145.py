import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
	time.sleep(1)
	print(f'thread_name')
t2 = datetime.now()

threads = [Thread(target = get_thread, args = (i+1, )) for i in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('time ', (datetime.now() - t2).microseconds)