import math

print(1 + 1 + 1 == 3)

is_ready = True

if (is_ready):
    print("is_ready is True")

texto = "computação"
if len(texto) > 10:
    print ("texto com mais de 10 caracteres")
else:
    print ("texto com 10 ou menos caracteres")

idade = 19
if (idade < 18):
    print ("Não pode tirar carteira de habilitação")
else:
    print ("Pode tirar a carteira de habilitação")

x = 10
print(x!=20)

y = 10
print("teste",x!=y)
print(x > y and x < y)
print(x > y or x < y)
print(x >= y or x <= y)
print(not (x == y))

a=0
b = 2
c = 1

if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")