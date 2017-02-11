# Number basic types on Python
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

# import pdb; pdb.set_trace()

# int type
x = 10
print("Variável x: ", x)
print("Tipo: ", type(x), "\n")

# float type
y = 20.
print("Variável y: ", y)
print("Tipo: ", type(y), "\n")

# complex type
z = 2 + 3j
print("Variável z: ", z)
print("Número Real: ", z.real)
print("Número Imaginário: ", z.imag)
print("Tipo: ", type(z), "\n")

result = y - x
print("y - x = ", result)
print("Tipo: ", type(result), "\n")

result = z + x
print("z + x = ", result)
print("Tipo: ", type(result), "\n")

result = x + y + z
print("x + y + z = ", result)
print("Tipo: ", type(result), "\n")

print("Métodos/atributos de X:", dir(x))
print("Métodos/atributos de Y:", dir(y))
print("Métodos/atributos de Z:", dir(z))
