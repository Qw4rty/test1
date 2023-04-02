#combo
import time
from threading import Thread
from datetime import datetime
from random import randint

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)

threads = [Thread(target = get_thread, args = ('thread'+str(randint(1,100)), )) for i in range(5)]
t1 = datetime.now()
for t in threads:
	t.start()
	t.join()
print(f'Время последовательного выполнения: {datetime.now()-t1}')

threads = [Thread(target = get_thread, args = ('thread'+str(randint(1,100)), )) for i in range(5)]
t1 = datetime.now()
for t in threads:
	t.start()
for t in threads:
	t.join()
print(f'Время параллельного выполнения: {datetime.now()-t1}')





