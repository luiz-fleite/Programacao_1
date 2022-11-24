
print("Jogo da velha")
# tabuleiro:
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f" {t[0]} | {t[1]} | {t[2]} \n"
      f" {t[3]} | {t[4]} | {t[5]} \n"
      f" {t[6]} | {t[7]} | {t[8]} \n")

# definindo os jogadores:
vencedor = True
j1 = input("Escolha X ou O: ")
j2 = None
if j1.upper() != "X" and j1.upper() != "O":
    print("Valor inválido.")
    vencedor = "X"
if j1.upper() == "X":
    j2 = "O"
else:
    j2 = "X"
j1 = j1.upper()
cont_jogadas = 0
while vencedor != "X" and vencedor != "O":
    # começando o jogo:
    # o jogador 1 começa inserindo obrigatóriamente uma coordenada válida no tabuleiro:
    coord = None
    while coord not in range(1, 10) or coord not in t:
        coord = int(input(f"{j1} Insira o número do tabuleiro onde quer colocar seu símbolo: "))
    # nesse caso é necessário garantir que a casa do tabuleiro é igual a coordenada, pois evita que o jogador trapaceie
    # escolhendo uma casa ocupada pelo adversário
    t[coord - 1] = j1
    # mostrando o tabuleiro com a jogada feita:
    print(f" {t[0]} | {t[1]} | {t[2]} \n"
          f" {t[3]} | {t[4]} | {t[5]} \n"
          f" {t[6]} | {t[7]} | {t[8]} \n")
    # verificando se houve vencedor:
    # ganhando na horizontal:
    for i in range(0, 6, 3):
        if t[i] == t[i + 1] == t[i + 2]:
            vencedor = j1
            print(f"{j1} venceu")
            break
    # ganhando na vertical:
    for i in range(3):
        if t[i] == t[i + 3] == t[i + 6]:
            vencedor = j1
            print(f"{j1} venceu")
            break
    # ganhando na diagonal:
    if t[0] == t[4] == t[8]:
        vencedor = j1
        print(f"{j1} venceu")
        break
    if t[2] == t[4] == t[6]:
        vencedor = j1
        print(f"{j1} venceu")
        break
    if vencedor == j1:
        break
    cont_jogadas += 1
    if cont_jogadas == 9:
        print("Velha")
        break
    cont_jogadas += 1
    if cont_jogadas == 9:
        print("Velha")
        break
    # caso não haja vencedor, a próxima jogada é do jogador 2:
    coord = None
    while coord not in range(1, 10) or coord not in t:
        coord = int(input(f"{j2} Insira o número do tabuleiro onde quer colocar seu símbolo: "))
    # nesse caso é necessário garantir que a casa do tabuleiro é igual a coordenada, pois evita que o jogador trapaceie
    # escolhendo uma casa ocupada pelo adversário
    t[coord - 1] = j2
    # mostrando o tabuleiro com a jogada feita:
    print(f" {t[0]} | {t[1]} | {t[2]} \n"
          f" {t[3]} | {t[4]} | {t[5]} \n"
          f" {t[6]} | {t[7]} | {t[8]} \n")
    # verificando se houve vencedor:
    # ganhando na horizontal:
    for i in range(0, 6, 3):
        if t[i] == t[i + 1] == t[i + 2]:
            vencedor = j2
            print(f"{j2} venceu")
            break
    # ganhando na vertical:
    for i in range(3):
        if t[i] == t[i + 3] == t[i + 6]:
            vencedor = j2
            print(f"{j2} venceu")
            break
    # ganhando na diagonal:
    if t[0] == t[4] == t[8]:
        vencedor = j2
        print(f"{j2} venceu")
        break
    if t[2] == t[4] == t[6]:
        vencedor = j2
        print(f"{j2} venceu")
        break
