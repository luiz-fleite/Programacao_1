morango = float(input("Insira o peso dos morangos em Kg: "))
maca = float(input("Insira o peso das maçãs em Kg: "))
preco1 = 0
preco2 = 0

if 0 < morango <= 5:
    preco1 = 2.5
elif morango > 5:
    preco1 = 2.2

if 0 < maca <= 5:
    preco2 = 1.8
elif maca > 5:
    preco2 = 1.5

valor_final_morango = morango * preco1
valor_final_maca = maca * preco2
valor_final_total = valor_final_morango + valor_final_maca

if morango + maca > 8 and valor_final_total > 25:
    valor_final_total *= 0.9  # Desconto 10%

print(f"Total a pagar: {valor_final_total:.2f}")
