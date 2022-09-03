n1, n2, n3 = float(input("Insira a primeira nota: ")),\
             float(input("Insira a segunda nota: ")),\
             float(input("Insira a terceira nota: "))
media = (n1 + n2 + n3) / 3
if media == 10:
    print("Aprovado com Disinção")
elif 7 <= media < 10:
    print("Aprovado")
else:
    print("Reprovado")
