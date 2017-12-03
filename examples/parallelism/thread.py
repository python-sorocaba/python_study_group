from time import sleep
from threading import Thread


class SlowThread(Thread):
    def __init__(self, number, *args, **kwargs):
        super(SlowThread, self).__init__(*args, **kwargs)
        self.number = number

    def run(self):
        for i in range(1, 11):
            print("Im thread {}: count {}".format(self.number, i))
            sleep(1)


if __name__ == '__main__':
    for number in range(1, 3):
        thread = SlowThread(number)
        thread.start()
