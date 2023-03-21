numeros = []
impar = 0
par = 0
for i in range(10):
  numeros.append(int(input(f"{i + 1}: ")))
  if numeros[i] % 2 != 0 or numeros[i] == 1:
    impar += 1
  else:
    par += 1
print(f"Impares {impar}\n"
      f"Pares {par}")
