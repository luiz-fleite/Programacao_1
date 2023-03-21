c = int(input())
print(f"Função: x1 + x2 = {c}\nSoluções possíveis:\n")
for i in range(c + 1):
  for j in range(c + 1):
    if i + j == c:
      print(f" x1 = {i}, x2 = {j}")
        