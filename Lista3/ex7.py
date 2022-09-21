salarios = []  # criando lista pra receber todos os salários
abonos = []  # criando lista pra receber todos os abonos
cont_abono_minimo = 0

while True:
    salario = float(input("Salário: "))
    if salario <= 0:
        break
    salarios.append(salario)

    abono = salario * 0.2
    if abono <= 100:
        abono = 100
        cont_abono_minimo += 1
    abonos.append(abono)

print()
print(f"Salário - Abono")
for i in range(len(salarios)):
    print(f"R$ {salarios[i]} - R$ {abonos[i]}")
print()
print(f"Foram processados {len(salarios)} colaboradores\n"
      f"Total gasto com abonos: R$ {sum(abonos)}\n"
      f"Valor mínimo pago a {cont_abono_minimo} colaboradores\n"
      f"Maior valor de abono pago: {max(abonos)}\n")
