from time import sleep
from concurrent.futures import ThreadPoolExecutor


def slow_function(number):
    for i in range(1, 3):
        print("Im {}: {}".format(number, i))
        sleep(1)

    return number


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        first_run = executor.submit(slow_function, 1)
        second_run = executor.submit(slow_function, 2)
        third_run = executor.submit(slow_function, 3)

        results = (first_run.result(), second_run.result(), third_run.result())
        print(results)
