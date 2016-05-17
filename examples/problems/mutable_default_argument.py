# Link for reference:
# http://stackoverflow.com/questions/9887180/the-value-of-an-empty-list-in-function-parameter-example-here

# Problem

print("Problem mutable default argument:")


def f(a, L=[]):
    L.append(a)
    print(id(L))
    return L

print(f(1, [1, 2]))  # expected [1, 2, 1] -> OK
print(f(1))  # expected [1] -> OK
print(f(2))  # expected [2] received [1, 2]-> NOK
print(f(3))  # expected [3] received [1, 2, 3] -> NOK

# Solution

print("Solution:")


def f(a, L=None):
    if not L:
        L = list()
    L.append(a)
    print(id(L))
    return L

print(f(1, [1, 2]))  # expected [1, 2, 1] -> OK
print(f(1))  # expected [1] -> OK
print(f(2))  # expected [2] -> OK
print(f(3))  # expected [3] -> OK
