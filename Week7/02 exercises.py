x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        print(y)
        y = y + 1
    x = x + 1

fora = 5
while fora > 0:
  dentro = 0
  while dentro < fora:
    print("oi")
    dentro = dentro + 1
  fora = fora - 1

def tabuada():
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print(tab,"x",i,"=",tab*i)
        print()

tabuada()

def exe4():
    x = 2
    cont = 0
    while x >= 0:
        y = 0
        while y >= 4:
            print(y)
            y = y + 1
        x = x - 1
exe4()

def exe6():
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            print(3*i+j+1,end=" ")
            j = j + 1
        print()
        i = i + 1
exe6()

def exe7():
    x = 1
    while x < 3:
        y = 1
        while y < 3:
            print(x*y, end = "\t")
            y = y + 1
        x = x + 1
exe7()