from random import randint


def matriz_gen(l, c):
    matriz = [[randint(0, 10) for j in range(c)] for i in range(l)]
    return matriz


a = matriz_gen(10, 10)
print("a: ", a)

# desempacotamento com if:
a_linear = [a[i][j] for i in range(10) for j in range(10) if a[i][j] != 0]
print(f"Itens não nulos: {a_linear}\nQuantidade de itens não nulos: {len(a_linear)}")
