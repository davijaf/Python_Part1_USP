for item in range(0,100,3):
    print(item)

for item in range(0,10):
    print(item)

pares = range(0,40,2)
for i in pares: print(i)

numeros = range(100,0,-5)
for x in numeros: print(x)

primos = [2, 3, 5, 7, 11, 13]
cube_primes = [0, 0, 0, 0, 0, 0]
for i in range(len(primos)):
    cube_primes[i] = primos[i]**3
print(cube_primes)
