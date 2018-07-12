import timeit

def for_implementation_ten():
    test = []
    for i in range(1,10):
        test.append(i)

def listcomp_implementation_ten():
    test = [i for i in range(1,10)]

def for_implementation_three():
    test = []
    for i in range(1,3):
        test.append(i)

def listcomp_implementation_three():
    test = [i for i in range(1,3)]

print("With ten elements, ", timeit.timeit(for_implementation_ten))
print("With ten elements, ", timeit.timeit(listcomp_implementation_ten))
print("With three elements, ", timeit.timeit(for_implementation_three))
print("With three elements, ", timeit.timeit(listcomp_implementation_three))

