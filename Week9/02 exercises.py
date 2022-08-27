a = "cavalo"
b = "cachorro"
c = "gato"
d = "cachorro"

print(a is c)
print(a is b)
print(b is d)
print(d is b)
print(c is a)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]
print("Second")
print(lista3 == lista1)
print(lista1 is lista2)
print(lista2 == lista1)
print(lista3 is lista2)
print(lista1 is lista3)
print(lista2 is lista3)
