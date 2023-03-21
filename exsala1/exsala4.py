import random
n = random.randrange(1, 101)

palpites = 1
meu_palpite = random.randrange(1, 101)
print(meu_palpite)

while meu_palpite != n:
  palpites += 1
  if meu_palpite > n:
    print("acima")
  elif meu_palpite < n:
    print("abaixo")
  meu_palpite = random.randrange(1, 101)
  print(meu_palpite)
print(f"Você acertou em {palpites} palpites")