peixe = float(input("Insira o peso dos peixes em kg: "))
excesso = peixe - 50
multa = excesso * 4
if (peixe <= 50):
    print(f"O peso do seu peixe foi {peixe}kg e não houve multa")
else:
    print(f"O peso do seu peixe foi {peixe}kg\n"
          f"Excesso de peso: {excesso}kg\n"
          f"multa: {multa}R$")