number = int(input("Enter a number for check is a Prime Number :"))
i = 2
prime = True
div = number
while i < number:
    div = div - 1
    i = i + 1
    if (number % div == 0):
        prime = False

if prime and number > 1:
    print("primo")
else:
    print("não primo")