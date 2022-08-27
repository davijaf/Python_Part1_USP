def partida(n,m):
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    iniciaJogo = True
    while n >= 0:
        if n % (m+1) == 0 and iniciaJogo:
            print("Você começa!")
            iniciaJogo = False
            usuario_escolhe_jogada(n,m)
        if iniciaJogo:
            iniciaJogo = False
            print("Computador começa!")
            computador_escolhe_jogada(n,m)
        else:
            return


def campeonato(n,m):
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    tipoJogo = input("Digite 1 ou 2 : ")
    while not tipoJogo.isdigit():
        print("Oops! Jogada inválida! Tente de novo.")
        tipoJogo = input("Digite 1 ou 2 : ")
    if int(tipoJogo) == 1:
        return partida(n,m)
    if int(tipoJogo) == 2:
        pontoUser = 0
        i  = 1
        while i <= 3:
            print("**** Rodada ",i," ****")
            partida(n,m)
            pontoPc = i
            i = i + 1
        print("**** Final do campeonato! ****")
        print("Placar: Você ",pontoUser," X ",pontoPc," Computador")
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        return campeonato(n,m)



def computador_escolhe_jogada(n,m):
    if n < 1:
        return print("Você ganhou!")
    pecasTabuleiro = n
    i = 0
    while i <= m:
        i += 1
        if (pecasTabuleiro-i) % (m+1) == 0:
            n = pecasTabuleiro - i
            i = m + 1
        else:
            n = pecasTabuleiro - m
    if n + 1 == pecasTabuleiro:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",pecasTabuleiro-n,"peças.")
    if n == 1:
        print("Agora restam uma peça no tabuleiro.")
    if n!=0 and n!=1:
        print("Agora restam",n,"peças no tabuleiro.")
    return usuario_escolhe_jogada(n,m)

def usuario_escolhe_jogada(n,m):
    if n < 1:
        return print("O computador ganhou!")
    else:
        userRemove = input("Quantas peças você vai tirar? ")
        while not userRemove.isdigit():
            print("Oops! Jogada inválida! Tente de novo.")
            userRemove = input("Jogador, quantas quer remover : ")
        while int(userRemove)<1 or int(userRemove)>m:
            print("Oops! Jogada inválida! Tente de novo.")
            userRemove = input("Quantas peças você vai tirar? ")
        n = n - int(userRemove)
    if int(userRemove) == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",int(userRemove),"peças.")
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    if n!=0 and n!=1:
        print("Agora restam",n,"peças no tabuleiro.")
    return computador_escolhe_jogada(n,m)



campeonato(3,1)