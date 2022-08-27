def n_primos(numbers):
    primes = 0
    while numbers >= 2:
        if prime(numbers) == True:
            primes = primes + 1
        numbers = numbers - 1
    return primes

def prime(number):
    i = 2
    prime = True
    div = number
    while i < number:
        div = div - 1
        i = i + 1
        if (number % div == 0):
            prime = False

    if prime and number > 1:
        return True
    else:
        return False

n_primos(6)