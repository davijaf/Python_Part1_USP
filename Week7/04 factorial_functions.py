def factorial():
    n = int(input("Enter a positive number: "))
    print("n","n!", end = "\t")
    print()
    while n >= 0:
        mult(n)
        n = int(input("Enter a positive number: "))
factorial()

def mult(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)