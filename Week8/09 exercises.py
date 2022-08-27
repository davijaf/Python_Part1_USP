alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(alfabeto)
print(len(alfabeto))

print(alfabeto[0:13])

letras = alfabeto[1:10]

print(letras)

print(alfabeto[13:])

print(alfabeto[13:27])

letras = alfabeto[:]

print(letras)

print(alfabeto[:13])

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)

carne = ["picanha", "alcatra", "filé mignon", "cupim"]
carne2 = []
for cns in carne:
    carne2.append(cns)
carne2.append("ponta de alcatra")

print(carne)
print(carne2)


carns = ["picanha", "alcatra", "filé mignon", "cupim"]
carns2 = carns[:]
carns2.append("ponta de alcatra")

print(carns)
print(carns2)


canes = ["picanha", "alcatra", "filé mignon", "cupim"]
canes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in canes:
    print("XXX")
else:
    if "ponta de alcatra" in canes2:
        print("YYY")
    else:
        print("ZZZ")

crnes1 = ["picanha", "alcatra"]
crnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
crnes3 = crnes2 + crnes1
print(crnes1)
print(crnes2)

pares = [2, 4, 6, 8, 10]
x = pares * 3
print(x)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
y = carnes
del (y[-1])

print(carnes)
print(y)
