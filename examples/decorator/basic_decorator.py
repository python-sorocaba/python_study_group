import logging
logging.basicConfig(filename='log_my_calls.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def log_call(func):
    logging.info("Call function {}".format(func.__name__))
    return func


@log_call
def my_sum(x, y):
    return x + y

if __name__ == "__main__":
    print(my_sum(10, 20))
