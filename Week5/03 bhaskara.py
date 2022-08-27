import math

a = float(input("Input cofficient a : "))
b = float(input("Input cofficient b : "))
c = float(input("Input cofficient c : "))
d = 1
if c > 0 and b > 0:
    print("Equation:",a,"* x^2","+",b,"* x","+",c,"= 0")
if c < 0 and b > 0:
    print("Equation:",a,"* x^2","+",b,"* x",c,"= 0")
if c > 0 and b < 0:
    print("Equation:",a,"* x^2",b,"* x","+",c,"= 0")
else:
    print("Equation:",a,"* x^2","+",b,"* x",c,"= 0")

def discriminant(a,b,c):
    return (b ** 2) - (4 * a * c)

def quadratic(a,b,c,d):
    return (-b + d * math.sqrt(discriminant(a,b,c))) / (2 * a)


if discriminant(a,b,c) >= 0:
    def x1(a,b,c,d):
        d = 1
        return quadratic(a,b,c,d)
    def x2(a,b,c,d):
        d = -1
        return quadratic(a,b,c,d)

    if discriminant(a,b,c) == 0:
        if x1(a,b,c,d) != x2(a,b,c,d):
            print("Roots of this function are",x1(a,b,c,d))
        elif x1(a,b,c,d) == x2(a,b,c,d):
            print("Root of this function is",x1(a,b,c,d))
    else:
        if x1(a,b,c,d) < x2(a,b,c,d):
            print("Function real roots are:",x1(a,b,c,d),"e",x2(a,b,c,d))
        else:
            print("Function real roots are:",x2(a,b,c,d),"e",x1(a,b,c,d))
else:
    print("Function doesn't real roots!")