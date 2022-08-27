def computador_escolhe_jogada(n, m):
    compRemove = 1

    while compRemove != m:
        if (n - compRemove) % (m+1) == 0:
            return compRemove

        else:
            compRemove += 1

    return compRemove

def usuario_escolhe_jogada(n, m):
    jogoValida = False

    while not jogoValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            jogoValida = True

    return jogadorRemove

print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada')
tipoPartida = int(input('2 - para jogar um campeonato '))

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    pcJoga = False

    if n % (m+1) == 0:
        print('Você começa!')

    else:
        print('Computador começa!')
        pcJoga = True

    while n > 0:
        if pcJoga:
            compRemove = computador_escolhe_jogada(n, m)
            n = n - compRemove
            if compRemove == 1:
                print('O computador tirou uma peça')
            else:
                print('O computador tirou', compRemove, 'peças')

            pcJoga = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print('Você tirou uma peça')
            else:
                print('Você tirou', jogadorRemove, 'peças')
            pcJoga = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')

    print('O computador ganhou!')

def campeonato():
    numRodada = 1
    while numRodada <= 3:
        print('**** Rodada', numRodada, '****')
        partida()
        numRodada += 1
    print('Placar: Você 0 X 3 Computador')

if tipoPartida == 2:
    print('Voce escolheu um campeonato!')
    campeonato()
else:
    if tipoPartida == 1:
        partida()
