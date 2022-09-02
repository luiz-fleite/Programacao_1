n = int(input("Insira o número: "))

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
if 0 < n < 8:
    print(dias[n - 1])
else:
    print("Valor inválido")
