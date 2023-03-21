n = int(input())
for i in range(n + 1):
  for j in range(1, i + 1):
    print("0", end= " ")
  print()
for i in range(1, n + 1):
  for j in range(1, n + 1 - i):
    print("1", end= " ")
  print()
    