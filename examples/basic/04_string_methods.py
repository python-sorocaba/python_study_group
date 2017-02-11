# String basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# import pdb; pdb.set_trace()
phrase = 'Introdução ao Python'

# spliting phrase into words
words = phrase.split()
print(phrase.split())
print(words[0])
print(words[1])
print(words[2])

# replacing strings
print(phrase.replace('Python', 'Python3'))

# using format
phrase = 'Hello {} {}!'
print(phrase.format('Rafael', 'Henrique'))

phrase = 'Hello {name} {surname}!'
print(phrase.format(surname='Henrique', name='Rafael'))

# using lower
phrase = 'STRING ' * 3
print(phrase.isupper())
print(phrase.islower())
print(phrase.lower())

# using upper
phrase = 'string ' * 3
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper())

# using title
phrase = 'rafael henrique da silva correia'
print(phrase.title())

# using isdigit / isalpha
phrase = 'Rafael 123'
print(phrase.isdigit())
print(phrase.isalpha())

phrase = '1234'
print(phrase.isdigit())

phrase = 'Rafael'
print(phrase.isalpha())

# endswith / startswith
phrase = 'Rafael 123'
print(phrase.endswith('123'))
print(phrase.endswith('3'))
print(phrase.endswith('4'))

print(phrase.startswith('Rafa'))
print(phrase.startswith('R'))
print(phrase.startswith('r'))
print(phrase.startswith('J'))
