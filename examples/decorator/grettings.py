def hello_decorator(func):
    def func_wrapper(name):
        return "Hello {0}".format(func(name))
    return func_wrapper


@hello_decorator
def hello(name):
    return "{}".format(name)


def say_name(name):
    return "{}".format(name)

if __name__ == "__main__":
    print(hello("Rafael"))
