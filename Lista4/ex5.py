from math import floor

# recebendo os limites de peso da categoria
inf_sup = input("Insira o limite inferior e superior de peso separados por espaço: ")
inf, sup = int(inf_sup.split()[0]), floor(int(inf_sup.split()[1]) * 1.08)  # calculando o limite superior da regra

# recebendo dados dos lutadores e salvando reprovados e o mais leve durante o processo
lutadores = {}
reprovados = []
mais_leve = [None, 999999]  # numero irreal pra garantir que o primeiro lutador entre no laço
n = int(input("Insira o número de lutadores: "))
for i in range(n):
    nome_peso = input(f"Insira o nome e o peso do lutador {i + 1} separados por espaço: ")
    nome, peso = nome_peso.split()[0], float(nome_peso.split()[1])
    lutadores[nome] = peso
    if lutadores[nome] < inf or lutadores[nome] > sup:
        reprovados.append(nome)
    elif lutadores[nome] < mais_leve[1]:
        mais_leve[0], mais_leve[1] = nome, lutadores[nome]

# printando a saida
print(f"Aprovados: {n - len(reprovados)}\n"
      f"Percentual de reprovados: {(len(reprovados) * 100) / n:.2f}%\n"
      f"Lutador mais leve: {mais_leve[0]}\n")
