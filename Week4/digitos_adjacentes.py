number = input("Enter a number :")
lengthNumber = len(number)
i = 0
equalDigits = False
while i < lengthNumber and not equalDigits:
    n1 = int(number) % 10
    number = int(number) // 10
    n2 = int(number) % 10
    i = i +1
    if n1 == n2 and (int(number) != 0):
        equalDigits = True

if equalDigits:
    print("sim")
else:
    print("não")