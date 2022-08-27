print("Let's calc binomial coefficient: n choose k")
n = int(input("Enter n for calc binomial coefficient : "))
k = int(input("Enter k for calc binomial coefficient : "))

def factor(z):
    factorial = 1
    y = 1
    while y <= z:
        factorial = y * factorial
        y = y + 1
    return factorial

def binomial(n,k):
    n = factor(n) / (factor(k)*factor(n-k))
    return n

x = int(binomial(n,k))

print("Binomial coefficient of",n,"/",k,"is",x)

if binomial(0,0) == 1:
    print(True)
else:
    print(False)

if binomial(9,5) == 126:
    print(True)
else:
    print(False)

if binomial(10,5) == 252:
    print(True)
else:
    print(False)

if binomial(10,10) == 1:
    print(True)
else:
    print(False)