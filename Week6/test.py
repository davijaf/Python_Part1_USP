def computador_escolhe_jogada(n,m):
    compRemove = 1
    while compRemove != m:
        if (n-compRemove) % (m+1) == 0:
            return compRemove
        else:
            compRemove += 1
    return compRemove

computador_escolhe_jogada(100,6)