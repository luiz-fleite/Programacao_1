area = float(input("Insira o valor da área a ser pintada em metros quadrados: "))
latas = area / 54  # 54 é 18 * 3, e representa a área pintada por 1 lata

if area % 54 != 0 or area < 54:  # arredondando pra cima sem usar biblioteca
    latas = int(latas + 1)

print(f"Quantidade de latas necessárias: {latas}\n"
      f"Preço a pagar: {latas * 80}R$")
