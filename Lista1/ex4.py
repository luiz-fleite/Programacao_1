n = []
for i in range(4):
    n.append(float(input(f"Insira a nota do {i + 1}º bimestre: ")))
print("Sua média é: ", sum(n) / len(n))
