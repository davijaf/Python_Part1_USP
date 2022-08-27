print("Type a values sequence")
numbers = int(input("How many numbers do you want add?"))
mult = 1
i = 0
while i < numbers:
    value = int(input("Type a number: "))
    mult = mult * value
    i = i + 1
    print("The sum of the input values is", mult)