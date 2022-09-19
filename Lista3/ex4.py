notas_alunos = []
gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

resp = input("Mensagem para o professor: Escolher gabarito? [s/n]")
if resp == "s":
    gabarito = []
    for i in range(10):
        gabarito.append((input(f"Insira a resposta de número {i +1}: ")).upper())

while True:
    resp_aluno = []
    ponto_aluno = 0

    for i in range(10):
        resp_aluno.append((input(f"Insira a resposta da questão {i +1}: ")).upper())

    for i in range(10):
        if resp_aluno[i] == gabarito[i]:
            ponto_aluno += 1

    notas_alunos.append(ponto_aluno)

    proximo = input("Próximo aluno? [s/n]")
    if proximo.lower() == "n":
        break

print(f"Maior número de acertos: ", max(notas_alunos))
print(f"Menor número de acertos: ", min(notas_alunos))
print("Total de alunos: ", len(notas_alunos))
print("Média de notas: ", sum(notas_alunos) / len(notas_alunos))
