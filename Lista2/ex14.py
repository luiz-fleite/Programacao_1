n1, n2 = float(input("Insira o primeiro número: ")), \
         float(input("Insira o segundo número: "))
op = int(input("Selecione a operação:\n"
               "1. Soma\n"
               "2. Subtração\n"
               "3. multiplicação\n"
               "4. Divisão\n"))
n3 = 0
if 1 > op > 4:
    print("Inválido")
elif op == 1:
    n3 = n1 + n2
elif op == 2:
    n3 = n1 - n2
elif op == 3:
    n3 = n1 * n2
elif op == 4:
    n3 = n1 / n2
print(n3)

if n3 == 0:
    print("O número é 0")
else:
    if n3 > 0:
        print("O número é positivo")
    else:
        print("O número é negativo")
    if n3 - int(n3) == 0:
        print("O número é inteiro")
        if n3 % 2 == 0 and n3 != 1:
            print("O número é par")
        else:
            print("O número é ímpar")
    else:
        print("O número é decimal")
