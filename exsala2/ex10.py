
def print_matriz(matriz):  # printar matriz formatada
    for i in range(len(matriz)):
        print(matriz[i])

def matriz_gen(l, c):
    matriz = [[float(input(f"Insira o elmento da linha {i} coluna {j}: ")) for j in range(c)] for i in range(l)]
    return matriz

l = int(input("Insira o numero de linhas: "))
c = int(input("Insira o numero de colunas: "))
a = matriz_gen(l, c)
print("a")
print_matriz(a)

l = int(input("Insira o numero de linhas: "))
c = int(input("Insira o numero de colunas: "))
b = matriz_gen(l, c)
print("b")
print_matriz(b)

# produto matriz
c = []
if len(a[0]) == len(b):
    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])):
            elemento = 0
            for k in range(len(a[0])):
                elemento += a[k][j] * b[i][k]
            linha.append(elemento)
        c.append(linha)

print("produto 1")
print_matriz(c)

c = [[[sum([a[k][j] * b[i][k] for k in range(len(a[0]))])] for j in range(len(b[0]))] for i in range(len(a))] if len(a[0]) == len(b) else False

print("produto 2")
print_matriz(c)

def matriz_produto(a, b):
    return [[[sum([a[k][j] * b[i][k] for k in range(len(a[0]))])] for j in range(len(b[0]))] for i in range(len(a))] if len(a[0]) == len(b) else False
