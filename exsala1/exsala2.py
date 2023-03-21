import random
n = random.randrange(1, 101)

palpites = 1
meu_palpite = int(input("Adivinhe: "))

while meu_palpite != n:
  palpites += 1
  if meu_palpite > n:
    print("acima")
  elif meu_palpite < n:
    print("abaixo")
  meu_palpite = int(input("de novo: "))
  if meu_palpite == 0:
    break
print(f"Você acertou em {palpites} palpites")