from random import randint

d = {}
reprovados = []
for i in range(3):
    k = 0  # variavel de controle pra incluir o reprovado na lista 1 vez
    d[f"estudante{i + 1}"] = []  # outra forma melhor seria armazenar no proprio dicionario a condição do aluno de
    # aprovado ou reprovado
    for j in range(3):
        nota = randint(500,1000) / 100  # fazendo um float aleatorio
        d[f"estudante{i + 1}"].append(nota)
        if nota < 7:
            if k == 0:
                reprovados.append(f"estudante{i + 1}")
                k += 1

print(d)
print(reprovados)
for x in d.keys():
    if x not in reprovados:
        print(f"{x} aprovado")
