
def matriz_gen(l, c):
    matriz = [[float(input(f"Insira o elmento da linha {i} coluna {j}: ")) for j in range(c)] for i in range(l)]
    return matriz


def matriz_sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


a = matriz_gen(int(input("Insira o numero de linhas: ")), int(input("Insira o numero de colunas: ")))
b = matriz_gen(int(input("Insira o numero de linhas: ")), int(input("Insira o numero de colunas: ")))

print(matriz_sub(a, b))
