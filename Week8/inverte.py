i = 1
j = 1
lista = []
while i > 0:
    i = int(input("Enter a number: "))
    lista.append(i)
while j < len(lista):
    x = len(lista) - j - 1
    j = j + 1
    print(lista[x])