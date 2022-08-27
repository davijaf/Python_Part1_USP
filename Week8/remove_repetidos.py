lista = [0, 2, 4, 2, 2, 3, 3, 1, 4, 2, 2, 3, 3, 1, 4, 2, 2, 3, 3, 1, 4, 2, 2, 3, 3, 1, 4, 2, 2, 3, 3, 1, 4, 2, 2, 3, 3, 1, 10, -1]

def remove_repetidos(lista):
    lista.sort()
    lista2 = []
    i = 0
    lista2.append(lista[0])
    while i < len(lista):
        if i+1 < len(lista):
            if lista[i] != lista[i+1]:
                lista2.append(lista[i+1])
        i = i + 1
    lista = lista2
    return lista

remove_repetidos(lista)