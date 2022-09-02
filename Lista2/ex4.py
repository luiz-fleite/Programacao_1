n1, n2 = float(input("Insira a primeira nota: ")), \
         float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2
conceito = "E"
if 0 <= media < 4:
    conceito = "E"
elif media < 6:
    conceito = "D"
elif media < 7.5:
    conceito = "C"
elif media < 9:
    conceito = "B"
elif media <= 10:
    conceito = "A"

print(f"Suas notas: {n1} e {n2}\n"
      f"Sua média: {media}\n"
      f"Seu conceito: {conceito}")
if conceito == "D" or conceito == "E":
    print("REPROVADO")
else:
    print("APROVADO")
