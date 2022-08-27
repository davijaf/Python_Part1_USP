line = 1
column = 1
while line <= 10:
    while column <=10:
        print(line,"*",column,"=",line*column,end ="\t")
        column = column + 1
    line = line + 1
    print()
    column = 1
