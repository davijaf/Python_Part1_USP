n = input("Enter a number for digits sum :")
ni = int(n)
i = 0
sum = 0

while i < len(n):
    sum = (ni % 10) + sum
    ni = ni // 10
    i = i + 1
print(sum)