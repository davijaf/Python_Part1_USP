number = input("Enter a number: ")
equalDigits = True if sorted(number) != sorted(set(number)) else False

if equalDigits:
    print("This number have a equal digits")
else:
    print("This number DON'T have a equal digits")
