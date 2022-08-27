
print("Exercise 01")
count = 0
while (count <= 10):
    print (count, "Olá Mundo!")
    count = count + 1

print("Exercise 02")
x = 10
while not (x == 0):
    x = x-1
    if x % 2 != 0:
      print (x)

print("Exercise 03")
i = 1
n = 3
while i < n:
      print("iteração")
      i = i + 1

print("Exercise 04")
terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)