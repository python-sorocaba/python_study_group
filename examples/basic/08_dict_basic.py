# Dict basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': ['a', 'b', 'c']}

print(type(my_dict))

# key in list
'a' in my_dict
'a' in my_dict.keys()
print(my_dict.keys())

# value in list
1 in my_dict.values()
print(my_dict.values())

# get value from key
print(my_dict.get('a'))
print(my_dict.get('z'))
print(my_dict.get('z', 'xablau!'))

print(my_dict['a'])
print(my_dict['z'])

# copy dict to another dict
new_dict = my_dict.copy()
print(new_dict)

# return values on tuple key, value
print(my_dict.items())

# remove element on X index with pop
A = my_dict.pop('a')
print(A)
print(my_dict)

# pop without raise TypeError
my_dict.pop()

# if key doesn't exists pop raise KeyError
Z = my_dict.pop('z')
print(Z)
print(my_dict)

# to prevent exception use pop with argument default
Z = my_dict.pop('z', 'Z value')
print(Z)
print(my_dict)

# popitem return last pair of key, value as tuple
my_dict = new_dict.copy()
print(my_dict)
A = my_dict.popitem()
print(A)
print(my_dict)

# setdefault try get a key, otherwise create a new one
my_dict.setdefault('a', 'jacaré')
print(my_dict)
my_dict.setdefault('z', 'jacaré')
print(my_dict)

# update try update if exist or create a new keys
my_dict.update({'z': 'zabumba', 'x': 'xuxa'})
print(my_dict)

# append elements in list associated with key 'd'
my_dict['d'].append('a')
print(my_dict)

# override values of one key
my_dict['d'] = 'Rafael'
print(my_dict)
