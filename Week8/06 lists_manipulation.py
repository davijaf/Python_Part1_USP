def n_primos(numbers):
    primes = 1
    primesArray = []
    while primes <= numbers:
        if prime(primes) == True:
            print(primes, end=", ")
            primesArray.append(primes)
        primes = primes + 1
    print(end="\n")
    print(primesArray)
    print(primesArray[1:2])
    print(primesArray[2:7])
    print(len(primesArray))
    print(primesArray[0:12])
    print(primesArray[12:25])
    print(primesArray[12:])
    final = primesArray[:12]
    print(final)

def prime(primes):
    i = 2
    prime = True
    div = primes
    while i < primes:
        div = div - 1
        i = i + 1
        if (primes % div == 0):
            prime = False

    if prime and primes > 1:
        return True
    else:
        return False

n_primos(100)