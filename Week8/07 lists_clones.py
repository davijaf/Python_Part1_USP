list1 = ["red","green","blue"]
list2 = list1
list2
print(list1)
list3 = list1[:] # clona a lista de maneira fácil
print(list2)
print(list1)
clone = []

#função clone abaixo pode ser substituida por list3 = list1[:]
def functionclone (x):
    clone = []
    for objeto in x:
        clone.append(objeto)
    print(clone)

functionclone(list1)
list2[2] = "rosa"
print(list1)

print(list3)

if "rosa" in list1:
    print("True")
else:
    print("False")


if "vermelho" in list1:
    print("True")
else:
    print("False")

print([1, 2]+[3, 4])

print([4, 3, 4, 5, 2]+[2, 4, 2, 4, 5, 6])

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

a.append(4)

print(a)

b = a + [5]

print(b)