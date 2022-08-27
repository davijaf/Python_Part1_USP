sideA = int(input("Enter a rectangle side A :"))
sideB = int(input("Enter a rectangle side B :"))
printSideA = 1
printSideB = 1
sideAprinted = "#"

while printSideA < sideA:
    sideAprinted = sideAprinted + "#"
    printSideA = printSideA + 1

while printSideB <= sideB:
    print(sideAprinted,end="\n")
    printSideB = printSideB + 1
