
# declara matriz
l = int(input("Insira o numero de linhas: "))
c = int(input("Insira o numero de colunas: "))
a = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(float(input(f"Insira o elemento da linha {i} coluna {j}: ")))
    a.append(linha)

print(a)

l = int(input("Insira o numero de linhas: "))
c = int(input("Insira o numero de colunas: "))
b = [[float(input(f"Insira o elmento da linha {i} coluna {j}: ")) for j in range(c)] for i in range(l)]

print(b)

def matriz_gen(l, c):
    matriz = [[float(input(f"Insira o elmento da linha {i} coluna {j}: ")) for j in range(c)] for i in range(l)]
    return matriz

# soma matriz

c = []
for i in range(len(a)):
    linha = []
    for j in range(len(a[0])):
        linha.append(a[i][j] + b[i][j])
    c.append(linha)

print("Soma 1: ")
print(c)

c = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print("Soma 2: ")
print(c)

def matriz_soma(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
