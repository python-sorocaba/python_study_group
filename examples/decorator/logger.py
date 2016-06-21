from datetime import datetime


def logger(func):
    def func_wrapper(x, y):
        return_func = func(x, y)
        date = datetime.now().strftime("%d-%m-%Y %T")
        msg = "{0} -> func_name {1}: Return {2}\n".format(date, func.__name__,
                                                          return_func)
        with open("log.txt", 'a') as fp:
            fp.write(msg)
        return return_func
    return func_wrapper


@logger
def sum(x, y):
    return x + y


@logger
def sub(x, y):
    return x - y


if __name__ == "__main__":
    print(sum(1, 2))
    print(sub(2, 1))
