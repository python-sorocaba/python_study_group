import random
from time import time, sleep
from multiprocessing import Process


def number():
    msg = "Number {} Time {}".format(
        random.randint(1, 100),
        time(),
    )
    print(msg)


def slow_function():
    for i in range(1, 11):
        print(i)
        sleep(1)


def run_parallel_functions(self, *functions):
    processes = []
    for function in functions:
        process = Process(target=function)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    run_parallel_functions(
        number(),
        number(),
        number(),
    )

    run_parallel_functions(
        slow_function(),
        slow_function(),
        slow_function(),
    )
