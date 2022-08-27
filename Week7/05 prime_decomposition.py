number = int(input("Enter a number for decomposition in prime numbers :"))
fator = 2
mult = 0
while number >= 2:
    while number % fator == 0:
        mult = mult + 1
        number = number / fator
    if mult > 0:
        print("fator", fator,"multiplicidade =",mult)
    fator = fator + 1
    mult = 0
