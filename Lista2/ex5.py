
L1, L2, L3 = float(input("Insira o valor do primeiro lado: ")), \
             float(input("Insira o valor do segundo lado: ")), \
             float(input("Insira o valor do terceiro lado: "))

print("O seu triângulo é: ")

if L1+L2 > L3 and L1+L3 > L2 and L2+L3 > L1:

    if L1 == L2 == L3:
      print("Equilátero")

    if L1 == L2 or L2 == L3 or L1 == L3:
      print("Isósceles")

    if L1**2+L2**2 == L3**2 or L2**2+L3**2 == L1**2 or L1**2+L3**2 == L2**2:
      print("Retângulo")

    if L1 != L2 != L3 != L1:
      print("Escaleno")

else:
 print("Quebrado, esses valores não formam triângulo")
