salario1 = float(input("Insira o valor do salário antigo: "))

salario2 = salario1
aumento = 0

if 0 < salario1 <= 280:
    aumento = 1.2
elif salario1 <= 700:
    aumento = 1.15
elif salario1 <= 1500:
    aumento = 1.1
elif salario1 > 1500:
    aumento = 1.05

salario2 *= aumento

print(f"Seu salário antigo: {salario1}R$\n"
      f"Seu aumento percentual: {(aumento - 1) * 100:.0f}%\n"
      f"Seu aumento em reais: {(salario2 - salario1):.2f}R$\n"
      f"Seu novo salário: {salario2}R$")
