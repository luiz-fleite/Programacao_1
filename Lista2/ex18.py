tipo = str(input("Insira o tipo da carne: [F/A/P] "))
kg = float(input("Insira a quantidade em Kg: "))
cartao = str(input("Cartão Tabajara? [sim/não]: "))

tipo = tipo.upper()
preco = 0
desc = 0

if tipo == "F":
    if 0 < kg <= 5:
        preco = 4.9
    elif kg > 5:
        preco = 5.8

if tipo == "A":
    if 0 < kg <= 5:
        preco = 5.9
    elif kg > 5:
        preco = 6.8

if tipo == "P":
    if 0 < kg <= 5:
        preco = 6.9
    elif kg > 5:
        preco = 7.8

valor_total = kg * preco
if cartao == "sim":
    valor_total *= 0.95
    desc = 5

print(f"Tipo de carne: {tipo}\n"
      f"Quantidade (Kg): {kg}\n"
      f"Cartão Tabajara: {cartao}\n"
      f"Desconto: {desc}%\n"
      f"Total a pagar: {valor_total}\n")
