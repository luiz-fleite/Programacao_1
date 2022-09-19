nomes = [["José", "João", "Maria", "Simone", "nulo", "branco"],
         [1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0]]

while True:
    voto = int(input("Voto: "))
    if voto == 0:
        break
    for j in range(6):
        if voto == nomes[1][j]:
            nomes[2][j] += 1

total_votos = sum(nomes[2])

for i in range(6):
    print(f"{nomes[0][i]}: {nomes[2][i]}\n")
print("Percentagem de nulos: ", int(nomes[2][4]) * 100 / total_votos)
print("Percentagem de brancos: ", int(nomes[2][5]) * 100 / total_votos)
