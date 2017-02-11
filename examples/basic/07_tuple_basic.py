# Tuple basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#tuples

my_tuple = ('Rafael Henrique da Silva Correia', 'Sorocaba', 'Cargo BR',
            'Sorocaba', (1988, 6, 14))

'Sorocaba' in my_tuple

# tuple is not mutable, this raise TypeError
my_tuple[0] = 'João'

# count 'Sorocaba'
print(my_tuple.count('Sorocaba'))

# find index of first 'Sorocaba'
print(my_tuple.index('Sorocaba'))

# unpack tuple
full_name, city, company, *_, (_, month, day) = my_tuple

message = (
    "Full name: {}\n"
    "City: {}\n"
    "Company: {}\n"
    "Birthday: {}/{}\n")
message = message.format(full_name, city, company, day, month)

print(message)
