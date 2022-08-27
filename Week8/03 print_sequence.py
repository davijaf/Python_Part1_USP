nElements = int(input("Enter the number of tens you want print :"))
tensArray = []
tens = 1
while tens <= nElements:
    element = tens * 10
    tensArray.append(element)
    tens += 1
print(tensArray)

i = 1
while i <= len(tensArray):
    x = len(tensArray) - i
    print(tensArray[x],end=", ")
    i += 1

for item in tensArray:
    print(item)