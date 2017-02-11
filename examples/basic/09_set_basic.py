# Set basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

A = {'a', 'b', 'c', 'd'}
B = {'a', 'b', '1', '2', '3'}

print(type(A))

# element in set
'a' in A
print(A)

# try add same element
A.add('a')
print(A)

# remove 'a' from A or raise KeyError if element doesn't exist
A.remove('a')
print(A)

# add removed element
A.add('a')
print(A)

# remove an element from A or do nothing
A.discard('a')
print(A)

# difference between sets
# dont change A and B
difference = A.difference(B)
print(difference)
print(A)
print(B)

# difference_update overwrite A set with difference between sets
A.difference_update(B)
print(A)
print(B)

A = {'a', 'b', 'c', 'd'}
B = {'a', 'b', '1', '2', '3'}

# intersection between A and B
# dont change A and B
interesection = A.intersection(B)
print(interesection)
print(A)
print(B)

# intersection_update overwrite A set with intersection between sets
A.intersection_update(B)
print(A)
print(B)

A = {'a', 'b', 'c', 'd'}
B = {'1', '2', '3'}

# check if sets are disjoint (opposite of intersection)
print(A.isdisjoint(B))

A = {'a', 'b', 'c', 'd'}
B = {'a', 'b', '1', '2', '3'}

# A union B
union = A.union(B)
print(union)

A = {'a', 'b', 'c', 'd'}
B = {'a', 'b'}

# check is set is a subset
print(B.issubset(A))
print(A.issubset(B))

# check is set is a superset
print(B.issuperset(A))
print(A.issuperset(B))

# A update with B, same result of union
A.update(B)
print(A)
