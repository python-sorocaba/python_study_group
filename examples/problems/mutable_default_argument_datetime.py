from datetime import datetime

print("Problem mutable default argument with datetime.now():")


def f(L=datetime.now()):
    print("Id: ", id(L))
    return L

print(f())
print(f('a'))
print(f(L=datetime(2016, 9, 13, 0, 0, 0)))
print(f(L=datetime(2016, 9, 13, 0, 0, 0)))
print(f(L=datetime(2016, 9, 13, 0, 0, 0)))
print(f()) ## PROBLEM: This datetime now is same of first
print(f()) ## PROBLEM: This datetime now is same of first
print(f()) ## PROBLEM: This datetime now is same of first

