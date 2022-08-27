from msvcrt import kbhit


def multiplica (a, b):
    return a * b

print(multiplica(4,5))

def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)

k = "1"
l = "23"
m = "456"

def total_Caracteres1(k, l, m):
    return len(k)+len(l)+len(m)
print(total_Caracteres1(k, l, m))

import math
o = 4
def suspense(o):
    return math.sqrt(o)
print(suspense(o))

def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
print(leitura())