descending = True
oldValue = int(input("Type a first sequence number :"))
value = oldValue
while value != 0 and descending:
    value = int(input("Type a next sequence number:"))
    if value > oldValue:
        descending = False
    oldValue = value

if descending == True:
    print("That's ok, descending order!")
else:
    print("Is not a descending order!")