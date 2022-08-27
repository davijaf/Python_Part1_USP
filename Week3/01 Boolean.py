print(5 > 3)
print(18 == 9*2)

print(type(False))

x = 12312
print(type(x > 0))
print(x > 0 and x**2 > 100)
print(x < 0 and x == 12312)

print(x < 0 or x == 12312)

print(not x > 0)

print(not False)
print(not True)

print(not not True)

sunny = True
holliday = False
gotoBeach = sunny and holliday
print(gotoBeach)

holliday = True
gotoBeach = sunny and holliday
print(gotoBeach)

promotion = True
fatherPay = False
gotoShow = fatherPay or promotion
print(gotoShow)

y = 50
print((x > 0) and (not y == 50) or (x + y == 150))


x = 10
y = 15
z = 25
print(x == z - y and z != y - x or not y != z - x)

x = 10
y = 20
z = 30
print(not y > 10 or not z > 10)
print(not y < 10 or not z == 10)
print(x >= 10 or y != z - x)
print(x <= 30 and y >= 5)

print(type(0))
print(type('0'))
print(type(True))
print(type(0.3))

a = 1
b = 2
print(a != 1 or b == 1)
print(a == 2 and b != 1)
print(not (a == 1))
print(a != 2 or b == 1)