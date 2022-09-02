for i in range(1):
    a = float(input("Insira o valor de a: "))
    if a == 0:
        print("A equação não é do segundo grau")
        break

    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))

    d = (b ** 2) - 4 * a * c
    if d < 0:
        print("A equação não possui raízes reais")
        break

    if d == 0:
        print("A equação possui apenas uma raíz real: ", -b / 2 * a)

    if d > 0:
        print("A equação possui duas raízes reais: \n",
            (-b + (d**0.5)) / 2 * a,
            (-b - (d**0.5)) / 2 * a)
