l = [1, 2, 3, 4, 5]
#print(l[5])
#print(l[7])
print(len(l))

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1

animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
for x in animais:
    print("--> ", x)

#for i in range(16,4,-3):
#    print(i)

#pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#for x in range(len(pares)):
#    print(pares[x])

#for i in range(0, 50, 5):
#	print(i)

#pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#for x in range(len(pares)):
#    print(x)

#pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#for x in range(5, 10):
#    print(pares[x])

valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)
print(valores)

valores = []
for i in range(2, 10, 2):
    valores.append(i)
print(valores)

valores = []
for i in range(1, 10, 2):
    valores.append(i)
print(valores)

valores = []
for i in range(0, 10, 2):
    valores.append(i)
print(valores)

valores = []
for i in range(1, 10):
    valores.append(i+1)
print(valores)

animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
animais[2] = animais.append("piriquito")
print(animais)