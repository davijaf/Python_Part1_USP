import math

def main():
    a = float(input("Input cofficient a : "))
    b = float(input("Input cofficient b : "))
    c = float(input("Input cofficient c : "))
    roots_print(a,b,c)

def discriminant(a,b,c):
    return (b ** 2) - (4 * a * c)

def quadratic(a,b,c,d):
    return (-b + d * math.sqrt(discriminant(a,b,c))) / (2 * a)

def roots_print(a,b,c):
    if discriminant(a,b,c) >= 0:
        def x1(a,b,c):
            d = 1
            return quadratic(a,b,c,d)
        def x2(a,b,c):
            d = -1
            return quadratic(a,b,c,d)

        if discriminant(a,b,c) == 0:
            if x1(a,b,c) != x2(a,b,c):
                print("Roots of this function are",x1(a,b,c))
            elif x1(a,b,c) == x2(a,b,c):
                print("Root of this function is",x1(a,b,c))
        else:
            if x1(a,b,c) < x2(a,b,c):
                print("Function real roots are:",x1(a,b,c),"and",x2(a,b,c))
            else:
                print("Function real roots are:",x2(a,b,c),"and",x1(a,b,c))
    else:
        print("Function doesn't real roots!")

main()