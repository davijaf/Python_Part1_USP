n = int(input("Enter a number for factorial calc :"))
factorial = 1
i = 1
y = n
while i < n:
    factorial = y * factorial
    y = y - 1
    i = i + 1
print(factorial)