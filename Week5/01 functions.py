from audioop import mul


def sum(x,y,z):
    return x + y + z
def multiple(x,y,z):
    return x * y * z

def yourTeam():
    print("Brazil")


print(sum(10,20,30))
print(sum(-20,100,40))

print(sum(-20,100,40)+multiple(20,30,10))
print(sum(-20,100,40),multiple(20,30,10))

yourTeam()

def quiet():
    x = 10 + 20
    print("The value of x is",x)
quiet()