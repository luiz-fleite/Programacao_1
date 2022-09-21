
def btomb(byt):
    mb = byt / 2 ** 20
    return mb


def porcent(maior, menor):
    p = menor * 100 / maior
    return p


with open("usuarios.txt", "r") as arquivo:
    tabela = arquivo.read()
tabela = tabela.split()
nomes = []
l_mb = []

for i in range(len(tabela)):
    if i % 2 == 0 and i != 1:
        nomes.append(tabela[i])
    else:
        l_mb.append(btomb(int(tabela[i])))

totalmb = sum(l_mb)
tabela2 = []
for i in range(len(nomes)):
    tabela2.append([nomes[i], round(l_mb[i], 2), round(porcent(totalmb, l_mb[i]), 2)])

with open("relatorio.txt", "w", encoding='utf-8') as arquivo:
    arquivo.write("ACME Inc. Uso do espaço em disco pelos usuários\n"
                  "--------------------------------------------------\n"
                  " Nr. Usuário         Espaço utilizado     % do uso\n")
    for i in range(len(tabela2)):
        arquivo.write(f" {i + 1}   {str(tabela2[i][0])} {(15 - len(str(tabela2[i][0]))) * ' '} "
                      f"{str(tabela2[i][1])}MB {(17 - len(str(tabela2[i][1]))) * ' '} "
                      f"{str(tabela2[i][2])}%\n")
    arquivo.write(f"\nEspaço total ocupado: {round(totalmb, 2)}MB\n"
                  f"Espaço médio ocupado: {round(totalmb / len(l_mb), 2)}MB")