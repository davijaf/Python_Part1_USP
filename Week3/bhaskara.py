import math

a = float(input("Input cofficient a : "))
b = float(input("Input cofficient b : "))
c = float(input("Input cofficient c : "))
discriminant = (b ** 2) - (4 * a * c)


if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    qe1 = a * x1**2 + b * x1 + c == 0
    qe2 = a * x2**2 + b * x2 + c == 0
    if discriminant == 0:
        if x1 != x2:
            print("a raiz dupla desta equação é",x1)
        else:
            print("a raiz desta equação é",x1)
    else:
        if x1 < x2:
            print("as raízes da equação são",x1,"e",x2)
        else:
            print("as raízes da equação são",x2,"e",x1)
else:
    print("esta equação não possui raízes reais")