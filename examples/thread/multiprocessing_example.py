import multiprocessing
import random
import time

def worker(num):
    """thread worker function"""
    print('Worker:', num)
    time.sleep(random.randint(1,3))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
