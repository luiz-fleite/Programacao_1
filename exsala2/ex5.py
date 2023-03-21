alunos = {}

resp1 = 's'
while resp1 == 's':
    nome = input("Insira o nome do aluno: ")
    alunos[nome] = []
    resp2 = 's'
    while resp2 == 's':
        alunos[nome].append(float(input("Insira a nota: ")))
        resp2 = input('Deseja continuar?[s/n]')
    resp1 = input('Deseja inserir outro aluno?[s/n]')

print(alunos)
    