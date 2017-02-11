# String basic examples on Python
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# import pdb; pdb.set_trace()

x = 'Rafael'
print("Variável x: ", x)
print("Tipo: ", type(x), "\n")

y = "Rafael"
print("Variável y: ", y)
print("Tipo: ", type(y), "\n")

z = """
Introdução ao Python
====================

Este é um teste de string multilinha
"""
print("Variável z: ", z)
print("Tipo: ", type(z), "\n")

# add more text to string
z += "\nMais um teste"
print(z)
