import math

def é_hipotenusa(number):
    i = 1
    hip = 0
    hipotenusa =  False
    while i < number:
        j = math.sqrt(number*number-i*i)
        if j.is_integer():
            #print(number,"^2 =",i,"^2 +",j,"^2")
            hipotenusa = True
            hip = number
        i = i + 1
    if hipotenusa:
        return hip
    else:
        return 0

def soma_hipotenusas(numbers):
    hipotenusas = 0
    while numbers >= 0:
        hipotenusas = hipotenusas + é_hipotenusa(numbers)
        numbers = numbers - 1
    return hipotenusas

soma_hipotenusas(25)
