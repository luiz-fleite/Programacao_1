p1, p2, p3, p4, p5, p6 = 0, 0, 0, 0, 0, 0
listanome = ["Cachorro quente", "Bauru Simples",
             "Bauru com ovo", "Hambúrguer", "Cheeseburguer", "Refrigerante"]
listap = [p1, p2, p3, p4, p5, p6]
print("Digite '0' para terminar")
while True:
    cod = int(input("Insira o código do item: "))

    if cod == 100:
        qtd = (int(input("Insira a quantidade: ")))
        p1 += qtd * 1.2

    elif cod == 101:
        qtd = (int(input("Insira a quantidade: ")))
        p2 += qtd * 1.3

    elif cod == 102:
        qtd = (int(input("Insira a quantidade: ")))
        p3 += qtd * 1.5

    elif cod == 103:
        qtd = (int(input("Insira a quantidade: ")))
        p4 += qtd * 1.2

    elif cod == 104:
        qtd = (int(input("Insira a quantidade: ")))
        p5 += qtd * 1.3

    elif cod == 105:
        qtd = (int(input("Insira a quantidade: ")))
        p6 += qtd

    elif cod == 0:
        break

listap = [p1, p2, p3, p4, p5, p6]

for i in range(7):
    if i in range(6):
        if listap[i] == 0:
            continue
        print(f"{listanome[i]}: R$ {listap[i]}")
    else:
        print("Total: R$ ", sum(listap))

