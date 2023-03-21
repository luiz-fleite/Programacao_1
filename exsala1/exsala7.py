c = int(input())
print(f"Função: x1 + x2 + x3 = {c}\nSoluções possíveis:\n")
for i in range(c + 1):
  for j in range(c + 1):
    for k in range(c + 1):
        if i + j + k == c:
            print(f" x1 = {i}, x2 = {j}, x3 = {k}")
            