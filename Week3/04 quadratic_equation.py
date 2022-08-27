import math

print("Hello, let's calculate quadratic equation!")
print("ax^2 + bx + c = 0")
print("x is discriminat")
print("Inputs the coefficients a, b and c!")

a = float(input("Input cofficient a : "))
b = float(input("Input cofficient b : "))
c = float(input("Input cofficient c : "))

discriminant = (b ** 2) - (4 * a * c)
print("Discriminant is",discriminant)

if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    qe1 = a * x1**2 + b * x1 + c == 0
    qe2 = a * x2**2 + b * x2 + c == 0
    if discriminant == 0:
        print("The root is real,",x1)
    else:
        print("The roots are reals,",x1,"and",x2)
else:
    print("The roots are unreals!")
