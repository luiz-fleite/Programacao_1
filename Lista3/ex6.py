atletas = []
total_notas = []

while True:
    notas = []  # armazena notas de um atleta
    nome = input("Insira o nome do atleta: ")
    if nome == '':  # termina o loop se não houver nome
        break
    atletas.append(nome)  # armazena nome válido

    for i in range(7):  # escreve as notas de um atleta
        x = - 1  # Simulando o 'do while'
        while 0 > x or x > 10:  # Ninguem pode tirar mais de 10, nem número negativo
            x = float(input(f"Insira a nota {i + 1}: "))
        notas.append(x)  # Adiciona valor válido
    total_notas.append(notas)  # salva as notas pra receber o próximo atleta

medias = []  # armazenas as medias pra encontrar o vencedor
for i in range(len(atletas)):
    print(f"Atleta: {atletas[i]}")
    numerais = ["Primeira", "Segunda", "Terceira",
                "Quarta", "Quinta", "Sexta", "Sétima"]  # pra printar corretamente sem repetir o codigo

    for j in range(7):
        print(f"{numerais[j]} nota: {total_notas[i][j]}")

    media = sum(sorted(total_notas[i])[1:6]) / 5  # armazena a media de cada atleta
    medias.append(media)  # salva a média pra achar o vencedor
    print()  # nova linha

media_maior = float(max(medias))
vencedor = atletas[medias.index(media_maior)]
print(f"Resultado final:\n"
      f"Atleta: {vencedor}\n"
      f"Melhor nota: {max(total_notas[atletas.index(vencedor)])}\n"
      f"Pior nota: {min(total_notas[atletas.index(vencedor)])}\n"
      f"Média: {media_maior:.2f}")
