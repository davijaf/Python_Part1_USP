# Nomes que não ajudam
def p(a):
    i = 0
    while i < len(a):
        if a[i] != a[len(a) - i - 1]:
            return False
        i = i + 1
    return True

# Nomes que ajudam a entender intuitivamente o problema
def eh_palindromo(palavra):
    letra = 0
    while letra < len(palavra):
        if palavra[letra] != palavra[len(palavra) - letra - 1]:
            return False
        letra = letra + 1
    return True

print(eh_palindromo("AMEOPOEMA"))

# if not media:
#    media = funcao_longa_que_calcula_a_media(media1, media2, media3,
#                                             media4, media5, media6)

#lucro = (vendas
#         + dividendos
#         - juros_divida
#         - salarios)

#minha_lista = [
#    1, 2, 3,
#    4, 5, 6,
#    ]

#minha_tupla = (
#    1, 2, 3,
#    4, 5, 6,
#)

# Não faça isso
#x+=1
# Ou isso
#x +=1
# Mas sim isso
#x += 1

# Não faça:
#x , y
#x [0]
#f( x )
## Faça
#x, y
#x[0]
#f(x)

# Comentário ruim:
#pos = pos + 1 #aumenta o contador em 1

# Comentário bom:
#pos = pos + 1  # Atualiza posição da nave espacial