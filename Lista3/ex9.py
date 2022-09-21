cont_mouse = 0
id_mouse = []
situacoes = []
n1, n2, n3, n4 = 0, 0, 0, 0
while True:
    id = int(input(f"Insira o id do mouse {cont_mouse + 1}: "))
    if id == 0:
        break
    id_mouse.append(id)
    cont_mouse += 1
    situacao = 0  # simulando 'do while'
    while situacao < 1 or situacao > 5:
        situacao = int(input(f"Insira a situação do mouse {cont_mouse}:\n"
                             f"1 - Esfera quebrada\n"
                             f"2 - sujo\n"
                             f"3 - Troca de cabo/conector\n"
                             f"4 - Inutilizado\n"))
        if situacao == 1:  # poderia usar o situacoes.count(1) etc... mas assim exige menos processamento
            n1 += 1
        elif situacao == 2:
            n2 += 1
        elif situacao == 3:
            n3 += 1
        elif situacao == 4:
            n4 += 1
    situacoes.append(situacao)

print(f"Quantidade de mouses: {cont_mouse}\n\n"
      f"Situação - quantidade - percentual\n"
      f"1- necessita de esfera - {n1} - {n1 * 100 / cont_mouse:.2f}%\n"
      f"2- necessita de limpeza - {n2} - {n2 * 100 / cont_mouse:.2f}%\n"
      f"3- necessita troca do cabo ou conector - {n3} - {n3 * 100 / cont_mouse:.2f}%\n"
      f"4- quebrado ou inutilizado - {n4} - {n4 * 100 / cont_mouse:.2f}%\n")
