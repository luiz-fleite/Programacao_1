'''mao1, mao2 = str(input("Insira o simbolo da primeira mão: ")), str(input("Insira o simbolo da segunda mão: "))
if mao1 == "pedra" and mao2 == "tesoura" or mao1 == "tesoura" and mao2 == "papel" or mao1 == "papel" and mao2 == "pedra":  print("mão 1 ganhou")
elif mao1 == mao2: print("empate")
else: print("mão 2 ganhou")'''

j1, j2 = int(input("Jogador 1, pedra 0, papel 1, tesoura 2: ")), int(input("Jogador 2, pedra 0, papel 1, tesoura 2: "))
if j1 == j2: print("empate")
elif((j1 - j2) % 3) == 1: print("jogador 1 ganhou")
else: print("jogador 2 ganhou")
    