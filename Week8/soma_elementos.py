from re import X


lista = [1, 2, 3, 4]
def soma_elementos(lista):
    x = 0
    for i in lista:
        x = i + x
    return x

soma_elementos(lista)