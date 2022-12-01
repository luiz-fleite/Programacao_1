import itertools, random

#Recebendo o valor de n:
n = int(input('Informe o número de cidades: '))

#Calculando as Combinações 2 a 2:
matriz = [[], []]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        matriz[0].append([i, j])

#Pedindo o t de cada cidade:
for i in matriz[0]:
    matriz[1].append(int(random.randint(1, 10)))

#Gerador de possibilidades de visitas sem considerar a condição k:
lista = [x for x in range(1, n+1)]
casos = [lista]
for i in range(2, len(lista)+1):
    for j in range(len(casos)):
        x = casos[j].copy()
        x.remove(i)
        x.insert(0, i)
        casos.append(x)

#Testando todas as possibilidades e vendo qual é a menor:
tempos = []
for p in casos:
    tempo = 0
    for i in range(len(p)-1):
        try:
            j = matriz[0].index([p[i], p[i+1]])
        except:
            j = matriz[0].index([p[i+1], p[i]])
        tempo += matriz[1][j]
    tempos.append(tempo)

#Printando o menor tempo que ele poderia ter executado uma rota tal que ela obedeça a condição proposta
print(f"O menor tempo possível seria: ", min(tempos))

'''color1 = colored.fg('red')
color2 = colored.fg('blue')
x = 9
contador = 0
for i in permutacoes:
    if i in invalidas:
        x = None
        #print(f"\033[0;31;40m{i}")
    else:
        print(f"\033[0;34;40m{i}")
        if i[0] == x:
            contador += 1
print(contador)'''

