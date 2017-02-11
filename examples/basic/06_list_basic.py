# List basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#lists

my_list = ['a', 'b', 'c', 1, 2, 3]

print(type(my_list))

# element in list
1 in my_list

# remove last element with pop
last_element = my_list.pop()
print(last_element)
print(my_list)

# remove element on X index with pop
first_element = my_list.pop(0)
print(first_element)
print(my_list)

# remove element by 'name'
c_element = my_list.remove('c')
print(c_element)  # return None
print(my_list)

# append element 'c' again
my_list.append('c')
print(my_list)

# insert element 'a' on index 0
my_list.insert(0, 'a')
print(my_list)

# sort elements, this cause TypeError, because cannot sort int with str
my_list.sort()

# sort elements with same type
numbers = [3, 4, 5, 10, 1, 2]
print(sorted(numbers))  # not in-place method
print(numbers)
numbers.sort()  # ATTENTION: in-place method
print(numbers)

alpha_chars = ['a', 'd', 'c', 'b']
print(sorted(alpha_chars))  # not in-place method
print(alpha_chars)
alpha_chars.sort()  # ATTENTION: in-place method
print(alpha_chars)

# reverse (invert) list elements with same type
print(sorted(alpha_chars, reverse=True))  # not in-place method
alpha_chars.reverse()  # ATTENTION: in-place method
print(alpha_chars)

# get index of element
print(alpha_chars.index('b'))

# count same elements on list
alpha_chars.append('b')
print(alpha_chars.count('b'))
print(alpha_chars.count('a'))
print(alpha_chars.count(0))

# merge all lists
all_lists = alpha_chars.copy() + numbers.copy() + my_list.copy()
print(all_lists)

# use extend to "sum" lists
fruits = ['jaca', 'maça']
fruit_names = ['abacaxi', 'laranja', 'uva']
fruits.extend(fruit_names)
print(fruits)

# clear list
fruits.clear()  # ATTENTION: in-place method
print(fruits)

# quantity of elements in list
print(len(all_lists))

# override value of index
all_lists[0] = 'Rafael'
print(all_lists)

# using unpack
name = "Rafael Henrique da Silva Correia"
first_name, *whatever = name.split()
print(first_name)
print(whatever)

first_name, second_name, *whatever = name.split()
print(first_name)
print(second_name)
print(whatever)

first_name, *middle, last_name = name.split()
print(first_name)
print(middle)
print(last_name)
