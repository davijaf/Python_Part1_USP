l = "a"
def vogal(l):
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        return True
    if l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
        return True
    else:
        return False

vogal(l)