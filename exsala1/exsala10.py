n = int(input("Insira o número de eleitores: "))
nomes = [["Bolsonaro", "Lula", "Ciro", "Simone Tebet", "Felipe", "Soraya"], [22, 13, 12, 15, 30, 44], [0, 0, 0, 0, 0, 0]]
for i in range(n):
  voto = int(input("Voto: "))
  for j in range(6):
    if voto == nomes[1][j]:
      nomes[2][j] += 1

for i in range(6):
  print(f"{nomes[0][i]}: {nomes[2][i]}\n")