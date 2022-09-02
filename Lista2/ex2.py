realhora = float(input("Insira o valor em reais ganho por hora de trabalho: "))
horas = float(input("Insira a quantidade de horas trabalhadas nesse mês: "))
sb = realhora * horas
tx = 0
if 0 < sb <= 900:
    tx = 0
elif sb <= 1500:
    tx = 5
elif sb <= 2500:
    tx = 10
elif sb > 2500:
    tx = 20
ir = sb * tx / 100
inss = sb * 0.1
fgts = sb * 0.11
descontos = ir + inss
print(f"Salário bruto: ({realhora} * {horas}): R$ {sb}\n"
      f"(-) IR({tx}%): R$ {ir}\n"
      f"(-)INSS(10%): R$ {inss}\n"
      f"FGTS (11%): R$ {fgts}\n"
      f"Salário Líquido: R$ {sb - descontos}")
