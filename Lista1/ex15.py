realhora = float(input("Insira o valor em reais ganho por hora de trabalho: "))
horas = float(input("Insira a quantidade de horas trabalhadas nesse mês: "))
sb = realhora * horas
ir = sb * 0.11
inss = sb * 0.08
sind = sb * 0.05
descontos = ir + inss + sind
print(f"+ Salário bruto: {sb}R$\n"
      f"- IR(11%): {ir}R$\n"
      f"- INSS(%8): {inss}R$\n"
      f"- Sindicato(5%): {sind}R$\n"
      f"= Salário Líquido: {sb - descontos}R$")
