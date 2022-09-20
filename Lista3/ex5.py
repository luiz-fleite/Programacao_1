atletas = []
total_saltos = []

while True:
    saltos = []  # armazena os saltos de um atleta
    nome = input("Insira o nome do atleta: ")
    if nome == '':  # termina o loop se não houver nome
        break
    atletas.append(nome)  # armazena nome válido

    for i in range(5):  # escreve os saltos de um atleta
        x = - 1  # Simulando o 'do while'
        while 0 > x or x > 10:  # Ninguem pularia mais de 10m de distância, nem número negativo
            x = float(input(f"Insira a distância do salto {i + 1}: "))
        saltos.append(x)  # Adiciona valor válido
    total_saltos.append(saltos)  # salva os saltos pra receber o próximo atleta

medias = []  # armazenas as medias pra encontrar o vencedor
for i in range(len(atletas)):
    print(f"Atleta: {atletas[i]}")
    numerais = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]  # pra printar corretamente sem repetir o codigo

    for j in range(5):
        print(f"{numerais[j]} salto: {total_saltos[i][j]}m")

    media = sum(sorted(total_saltos[i])[1:4]) / 3  # armazena a media de cada atleta
    medias.append(media)  # salva a média pra achar o vencedor
    print(f"Melhor salto: {max(total_saltos[i])}m\n"
          f"Pior salto: {min(total_saltos[i])}m\n"
          f"Média dos demais saltos: {media}m\n")

media_maior = float(max(medias))
vencedor = atletas[medias.index(media_maior)]
print(f"Resultado final:\n"
      f"{vencedor}: {media_maior:.2f}m")
