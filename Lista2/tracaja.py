vtracaja = []
n = 0
while n not in range(1, 50):
    n = int(input("Insira o número de tracajás: "))

for i in range(n):
    v = 0
    while v not in range(1, 25):
        v = int(input(f"Insira a velocidade do tracajás {i + 1}: "))
    vtracaja.append(v)

maior = max(vtracaja)
if maior < 10:
    print(1)
elif maior < 15:
    print(2)
elif maior > 15:
    print(3)
