a = float(input("Insira a quantidade de litros de álcool: "))
g = float(input("Insira a quantidade de litros de gasolina: "))

preco_a = 1.9
preco_g = 2.5
d_a = 0
d_g = 0

if 0 < a <= 20:
    d_a = 0.03
elif 20 < a:
    d_a = 0.05

if 0 < g <= 20:
    d_g = 0.04
elif 20 < g:
    d_g = 0.06

custo_final_a = (preco_a - preco_a * d_a) * int(a) + (preco_a * (a - int(a)))
custo_final_g = (preco_g - preco_g * d_g) * int(g) + (preco_g * (g - int(g)))

print(f"Valor a pagar:\n"
      f"A- R$ {custo_final_a:.2f}\n"
      f"G- R$ {custo_final_g:.2f}\n")
