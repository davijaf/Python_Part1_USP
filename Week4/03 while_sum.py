print("Type a values sequence")
numbers = int(input("How many numbers do you want to add?"))
sum = 0
i = 0
while i < numbers:
    value = int(input("Type a number: "))
    sum = sum + value
    i = i + 1
    print("The sum of the input values is", sum)