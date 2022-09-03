controle = 0
r = str(input("Telefonou pra vítima? [sim/não] "))

if r == "sim":
    controle += 1
r = str(input("Esteve no local do crime? [sim/não] "))
if r == "sim":
    controle += 1
r = str(input("Mora perto da vítima? [sim/não] "))
if r == "sim":
    controle += 1
r = str(input("Devia pra vítima? [sim/não] "))
if r == "sim":
    controle += 1
r = str(input("já trabalhou com a vítima? [sim/não] "))
if r == "sim":
    controle += 1

if controle == 0:
    print("Inocente")
elif controle <= 2:
    print("Suspeito")
elif controle <= 4:
    print("Cúmplice")
elif controle == 5:
    print("Assassino")
