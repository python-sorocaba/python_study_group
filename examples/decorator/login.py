
def login_required(func):
    def func_wrapper(x, y):
        return_func = func(x, y)
        if USER == "admin" and PASS == "123":
            pass
        else:
            raise Exception("Login failed!")
        return return_func
    return func_wrapper


@login_required
def sum(x, y):
    return x + y

if __name__ == "__main__":
    USER = input("Informe usuario: ")
    PASS = input("Informe senha: ")
    print(sum(1, 2))
