import itertools, random
import colored
#  Recebendo o valor de n:
'''n = int(input('Informe o número de cidades: '))
#  Calculando as Combinações 2 a 2:
matriz = [[], []]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        matriz[0].append([i, j])
#  Pedindo o t de cada cidade:
for i in matriz[0]:
    matriz[1].append(int(random.randint(1, 10)))
#  Gerador de possibilidades de visitas sem considerar a condição k:
'''
'''
lista = [i for i in range(1, 101)]
casos = [lista]
for i in range(2, len(lista)+1):
    for j in range(len(casos)):
        x = casos[j].copy()
        x.remove(i)
        x.insert(0, i)
        casos.append(x)
print(casos)
'''

vx = []
x = input("Insira o numero de andares e o numero de eventos separados por espaço: ")
lista = x.split(' ')
print(lista)
for i in range(2):
    vx.append(int(x[i]))
print(vx)
