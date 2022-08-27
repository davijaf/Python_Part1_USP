myCard = int(input("Type a credit card number :"))

cardRead = 1
foundMyCard = False

while cardRead != 0 and not foundMyCard:
    cardRead = int(input("Type next credit card number :"))
    if cardRead == myCard:
        foundMyCard = True

if foundMyCard:
    print("Yes, i found my card!")
else:
    print("No, my card not found!")