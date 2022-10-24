from random import randint

d = {}
for i in range(1, 7):
    d[f"c{i}"] = []

melhor_volta = [0, 999]  # o numero aq deve ser maior q o tempo de uma volta qualquer
for corredor in d.keys():
    for i in range(10):
        d[corredor].append(randint(1000, 6000) / 100)  # fazendo um float aleatorio
        if d[corredor][i] < melhor_volta[1]:
            melhor_volta = [corredor, d[corredor][i], i + 1]

print(d)
print(min)

dpodio = {}
for corredor, voltas in d.items():
    dpodio[corredor] = sum(voltas) / 10

print(f"O corredor {melhor_volta[0]} fez {melhor_volta[1]}s na "
      f"sua {melhor_volta[2]}a volta. Sendo essa a melhor volta de todas.")
i = 0
for corredor in sorted(dpodio, key=dpodio.get):
    i += 1
    print(f"{i}º Lugar: {corredor}. Tempo: {dpodio[corredor]}s")

# outra forma q não consegui usar...
'''podio = [[], []]
for corredor, voltas in d.items():
    podio[0].append(corredor)
    podio[1].append(sum(voltas) / 10)
print(f"O corredor {min[0]} fez {min[1]}s na sua {min[2]}a volta. Sendo essa a melhor volta de todas.")
for i in range(10):
    print(f"{i + 1}o Lugar: 
    {podio[0].pop(podio[0][podio[1].index(min(podio[1]))])} Tempo: {podio[1].pop(min(podio[1]))}")'''
