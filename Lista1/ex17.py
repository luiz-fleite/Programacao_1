area = float(input("Insira o valor da área a ser pintada em metros quadrados: "))

# calculando para apenas latas:
latas = area / 108  # 108 é 18 * 6, e representa a área pintada por 1 lata
solatas = int(latas)

if latas - solatas != 0:  # arredondando pra cima sem usar biblioteca
    solatas += 1

# calculando pra apenas galões:
sogaloes = area / 21.6  # 21.6 é 3.6 * 6, e representa a área pintada por 1 galão

if sogaloes - int(sogaloes):  # arredondando pra cima sem usar biblioteca
    sogaloes = int(sogaloes + 1)

# calculando a mistura:
latas *= 0.9  # criando a folga de 10%
restoarea = (latas - int(latas)) * 108
galoes = restoarea / 21.6  # pintando o que sobrou com galão

if galoes - int(galoes) != 0:  # arredondando pra cima sem usar biblioteca
    galoes = int(galoes + 1)
    if galoes == 5:
        galoes = 0
        latas += 1

print(f"Apenas latas: {solatas}\n"
      f"Preço: {solatas * 80}R$\n"
      f"Apenas galões: {sogaloes}\n"
      f"Preço: {sogaloes * 25}R$\n"
      f"Mistura econômica:\n"
      f"Latas: {int(latas)}\n"
      f"Galões: {galoes}\n"
      f"Preço da mistura: {int(latas) * 80 + galoes * 25}R$")
