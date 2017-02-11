# String basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# import pdb; pdb.set_trace()
phrase = 'Introdução ao Python'

# reverse string using slicing
print(phrase[::-1])

# getting slices
print(phrase[0:11])
print(phrase[11:14])
print(phrase[14:20])

# omiting initial and final
print(phrase[:11])
print(phrase[11:14])
print(phrase[14:])

# get up 2 in 2
print(phrase[::2])

# get up reverse 2 in 2
print(phrase[::-2])

palindrom = 'ANOTARAM A DATA DA MARATONA'
print(palindrom[::-1])
print(palindrom)
