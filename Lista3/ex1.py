n = 1
lista = []
while n >= 0:
    n = int(input("Insira o n: "))
    lista.append(n)

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

for i in lista:
    if i in range(26):
        cont1 += 1
    if i in range(26, 51):
        cont2 += 1
    if i in range(51, 76):
        cont3 += 1
    if i in range(76, 101):
        cont4 += 1

print(cont1, cont2, cont3, cont4)