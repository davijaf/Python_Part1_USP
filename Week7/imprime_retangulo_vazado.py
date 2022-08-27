sideA = int(input("Enter a rectangle side A :"))
sideB = int(input("Enter a rectangle side B :"))
printSideA = 1
printSideB = 1
printSideAempty = 1
sideAprinted = "#"
sideAempty = "#"

while printSideA < sideA:
    sideAprinted = sideAprinted + "#"
    printSideA = printSideA + 1

while printSideAempty < sideA:
    if printSideAempty == sideA -1:
        sideAempty = sideAempty + "#"
    else:
        sideAempty = sideAempty + " "
    printSideAempty = printSideAempty + 1


while printSideB <= sideB:
    if printSideB == 1 or printSideB == sideB:
        print(sideAprinted,end="\n")
        printSideB = printSideB + 1
    else:
        print(sideAempty,end="\n")
        printSideB = printSideB + 1
