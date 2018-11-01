import  threading
from queue import Queue
import time


q = Queue()


def exampleJob(worker):
    time.sleep(0.5)

    with threading.Lock():
        print(threading.current_thread().name , worker)

def work():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

for _ in range(10):
    t= threading.Thread(target=work)
    t.daemon = True

    t.start()

start_time = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print("Elapsed time took: ", time.time() - start_time)