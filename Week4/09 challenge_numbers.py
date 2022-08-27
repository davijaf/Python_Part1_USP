number = input("Enter a number :")
lengthNumber = len(number)
i = 0
equalDigits = False
while i < lengthNumber and not equalDigits:
    n1 = int(number) % 10
    number = int(number) // 10
    n2 = int(number) % 10
    i = i +1
    if n1 == n2:
        equalDigits = True

if equalDigits:
    print("This number have a equal digits in sequence")
else:
    print("This number DON'T have a equal digits in sequence")