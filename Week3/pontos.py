import math

x1 = int(input("Type a x1 coordinate: "))
y1 = int(input("Type a y1 coordinate: "))
x2 = int(input("Type a x2 coordinate: "))
y2 = int(input("Type a y2 coordinate: "))

distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(distance)
if distance >= 10:
    print("longe")
else:
    print("perto")