from random import randint

d = {}
for i in range(1, 6):
    d[f"c{i}"] = []

melhor_volta = [0, 999]  # o numero aq deve ser maior q o tempo de uma volta qualquer
for corredor in d.keys():
    for i in range(10):
        d[corredor].append(randint(1000, 6000) / 100)  # fazendo um float aleatorio
        if d[corredor][i] < melhor_volta[1]:
            melhor_volta = [corredor, d[corredor][i], i + 1]

dpodio = {}
for corredor, voltas in d.items():
    dpodio[corredor] = sum(voltas) / 10

print(f"O corredor {melhor_volta[0]} fez {melhor_volta[1]}s na "
      f"sua {melhor_volta[2]}a volta. Sendo essa a melhor volta de todas.")
i = 0
for corredor in sorted(dpodio, key=dpodio.get):
    i += 1
    print(f"{i}º Lugar: {corredor}. Tempo: {dpodio[corredor]}s")


'''# tentei usar comprehensios...
for i in range(6):
    a[input(f"Insira o nome do corredor {i + 1}: ")] = [randint(400, 1000) / 100 for j in range(10)]'''
