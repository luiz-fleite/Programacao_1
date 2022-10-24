

def incluirnovonome(name, tels):
    agenda[name] = tels


def incluirtelefone(name):
    if name in agenda:
        r = "s"
        while r.lower() == "s":
            agenda[name].append(input("insira o telefone: "))
            r = input("Deseja inserir mais um telefone?[s/n]")
    else:
        r = int(input("O nome não está na agenda, deseja incluir?[s/n]"))
        if r == "s":
            telefones = []
            r = "s"
            while r.lower() == "s":
                telefones.append(input("insira o telefone: "))
                r = input("Deseja inserir mais um telefone?[s/n]")
            incluirnovonome(name, telefones)


def excluirtelefone(name, tel):
    if name in agenda:
        if tel in agenda[nome]:
            agenda[nome].remove(tel)
            if len(agenda[nome]) == 0:
                excluirnome(nome)
            else:
                print(f"Novo:\n{nome}: {agenda[nome]}")
        else:
            print("Valor inválido.")
    else:
        print("Nome não encontrado")


def excluirnome(name):
    if name in agenda:
        del agenda[name]
    else:
        print("Nome não encontrado")


def consultartelefone(name):
    if name in agenda:
        print(agenda[name])
    else:
        print("Nome não encontrado")


agenda = {}
while True:
    f = input("O que deseja fazer na agenda?\n"
              "0- Sair;\n"
              "1- Incluir novo nome;\n"
              "2- Incluir telefone;\n"
              "3- Excluir telefone;\n"
              "4- Excluir nome;\n"
              "5- Consultar telefone.\n")

    if f == '0':
        break

    elif f == '1':
        nome = input("Qual o nome da pessoa? ")
        telefones = []
        r = "s"
        while r.lower() == "s":
            telefones.append(input("insira o telefone: "))
            r = input("Deseja inserir mais um telefone?[s/n]")
        incluirnovonome(nome, telefones)

    elif f == '2':
        incluirtelefone(input("Qual o nome da pessoa? "))

    elif f == '3':
        nome = input("Qual o nome da pessoa? ")
        telefone = input(f"Digite o telefone que deseja excluir:\n{agenda[nome]}\n")
        excluirtelefone(nome, telefone)

    elif f == '4':
        excluirnome(input("Qual o nome da pessoa que deseja excluir? "))

    elif f == '5':
        consultartelefone(input("Qual o nome da pessoa que deseja ver os números? "))

    else:
        print("Valor inválido.")
