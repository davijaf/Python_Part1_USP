def factorial():
    n = int(input("Enter a positive number: "))
    print("n","n!", end = "\t")
    print()
    while n >= 0:
        fatorial = 1
        while n > 1:
            fatorial = fatorial * n
            n = n - 1
        print(fatorial)
        n = int(input("Enter a positive number: "))
factorial()