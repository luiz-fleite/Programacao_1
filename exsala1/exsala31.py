texto = input("insira o texto: ")
pontos = [",", ".", ";", ":", "'"]
for i in list(texto):
  if i in pontos:
      texto = texto.replace(i, '')
print(len(texto.split()))