def prime(n):
    i = 2
    div = n
    p = True
    while i < n:
        div = div - 1
        i = i + 1
        if (n % div == 0):
            p = False

    if p and n > 1:
        return True
    else:
        return False

def maior_primo(n):
    while not prime(n):
        n = n - 1
        prime(n)
    return n

maior_primo(100)