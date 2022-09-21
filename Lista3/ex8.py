modelos = []
km_ls = []
for i in range(5):
    modelo = input(f"Veículo {i + 1}\nNome: ")
    km_l = float(input("Km por litro: "))
    modelos.append(modelo)
    km_ls.append(km_l)

print("Relatório final:")
for i in range(5):
    print(f"{i + 1} - {modelos[i]} - {km_ls[i]} - {1000 / km_ls[i]:.2f} litros - R$ {1000 / km_ls[i] * 2.25:.2f}")
print(f"O menor consumo é do {modelos[km_ls.index(max(km_ls))]}.")
