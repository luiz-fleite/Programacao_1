valor = int(input("Insira o valor do saque: "))

if valor >= 100:
    print(f"Notas de 100: {valor // 100}")
    valor -= (valor // 100) * 100
if valor >= 50:
    print(f"Notas de 50: {valor // 50}")
    valor -= (valor // 50) * 50
if valor >= 10:
    print(f"Notas de 10: {valor // 10}")
    valor -= (valor // 10) * 10
if valor >= 5:
    print(f"Notas de 5: {valor // 5}")
    valor -= (valor // 5) * 5
if 0 < valor < 5:
    print(f"Notas de 1: {valor}")
