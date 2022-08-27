number = input("Type a number for sum of decomposition values:")
length = len(number)
sum = 0
i = 0

while i < length:
    numberDec = int(number) % 10
    sum = numberDec + sum
    number = int(number) // 10
    i = i + 1

print("The sum elements of number decomposition is:", sum)
