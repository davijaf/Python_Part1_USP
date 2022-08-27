def partida(n,m):
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    iniciaJogo = True
    while n >= 1:
        if n % (m+1) == 0 and iniciaJogo:
            iniciaJogo = False
            jogadorJoga = True
            print("Você começa!")
        if iniciaJogo:
            iniciaJogo = False
            jogadorJoga = False
            print("Computador começa!")
        if jogadorJoga and n != 0:
            jogadorJoga = False
            jogadorRemove = int(usuario_escolhe_jogada(n,m))
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",jogadorRemove,"peças.")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if n!=0 and n!=1:
                print("Agora restam",n,"peças no tabuleiro.")
        if not jogadorJoga and n != 0:
            jogadorJoga = True
            computadorRemove = int(computador_escolhe_jogada(n,m))
            n = n - computadorRemove
            if computadorRemove == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",computadorRemove,"peças.")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if n!=0 and n!=1:
                print("Agora restam",n,"peças no tabuleiro.")
    if jogadorJoga and n == 0:
        print("O computador ganhou!")
        return jogadorJoga
    else:
        print("Você ganhou!")
        return jogadorJoga


def computador_escolhe_jogada(n,m):
    compRemove = 1
    while compRemove != m:
        if (n-compRemove) % (m+1) == 0:
            return compRemove
        else:
            compRemove += 1
    return compRemove

def usuario_escolhe_jogada(n,m):
        userRemove = input("Quantas peças você vai tirar? ")
        while not userRemove.isdigit():
            print("Oops! Jogada inválida! Tente de novo.")
            userRemove = input("Jogador, quantas quer remover : ")
        while int(userRemove)<1 or int(userRemove)>m:
            print("Oops! Jogada inválida! Tente de novo.")
            userRemove = input("Quantas peças você vai tirar? ")
        return userRemove


def campeonato(n,m):
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    tipoJogo = input()
    while not tipoJogo.isdigit():
        print("Oops! Jogada inválida! Tente de novo.")
        tipoJogo = input("Digite 1 ou 2 : ")
    if int(tipoJogo) == 1:
        print("Você escolheu partida isolada!")
        return partida(n,m)
    if int(tipoJogo) == 2:
        print("Voce escolheu um campeonato!")
        pontoUser = 0
        pontoPc = 0
        i  = 1
        while i <= 3:
            print("**** Rodada ",i," ****")
            x = partida(n,m)
            i = i + 1
            if x:
                pontoPc = pontoPc + 1
            else:
                pontoUser = pontoUser + 1
        print("**** Final do campeonato! ****")
        print("Placar: Você ",pontoUser," X ",pontoPc," Computador")
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        return campeonato(n,m)

campeonato(3,1)