import re
digitos = re.search(r'\d+','programação1 é a disciplina + importante para rac3ocínio l0gic0')
print(digitos)

digitos = re.search(r'\d+',' é a disciplina + importante para rac3ocínio l0gic0')
print(digitos)

digitos = re.search(r'\d+','programação é a disciplina + importante para racocínio')
print(digitos)

digitos = re.search(r'\d+','programação1234567770978 é a disciplina + importante para rac3ocínio l0gic0')
print(digitos)

digitos = re.search(r'\d+','programação é a disciplina + importante para racocínio')
print(digitos)
if digitos:
    print("Sim", digitos)
else:
    print("Não", digitos)

digitos = re.search(r'\d+','programação123 é a disciplina + importante para racocínio')
print(digitos)
if digitos:
    print("Sim", digitos)
else:
    print("Não", digitos)

digitos = re.search(r'\d+', 'Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos.span())
print(digitos.group())

digitos = re.search(r'\d+', '- Guamá. CEP 66075-110')
print(digitos.span())
print(digitos.group())

digitos = re.search(r'\d+', '- Guamá. CEP 66075110')
print(digitos.span())
print(digitos.group())

digitos = re.match(r'\d+', 'Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos)
# encontra apenas no começo
digitos = re.match(r'\d+', '09 Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos)

digitos = re.sub(r'\d+','V', 'Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos)

digitos = re.findall(r'\d+', 'Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos)

digitos = re.split(r'\d+', 'Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(digitos)
# ganho de eficiência pra muitos dados processados
dd = re.compile(r'\d+')
dados = dd.search('Rua augusto Corrêa, 01 - Guamá. CEP 66075-110')
print(dados)

dd = re.compile(r'\d+')
dados = dd.search('Rua augusto Corrêa, 01 - Guamá. CEP 66075-110', 22)  # definindo o índice do começo da busca no segundo argumento
print(dados)
# o ponto '.' significa 'qualquer caractere'
regex = re.compile(r'.ão')
dados = regex.search('O cão')
print(dados)

dados = regex.search('O cão são')
print(dados)

dados = regex.search('O pão')
print(dados)

dados = regex.search('O 3cão')
print(dados)

dados = regex.search('ão')
print(dados)

dados = regex.search('426624ão')
print(dados)
# o colchete '[]' significa 'lista de possibilidades'
regex = re.compile(r'p[aã]o')
dados = regex.search('O pão')
print(dados)

dados = regex.search('O po')
print(dados)

dados = regex.search('O seu pao')
print(dados)

dados = regex.search('paão')
print(dados)
# o colchete '[]' com menos '-' no centro representa um intervalo
regex = re.compile(r'Turma[0-9]')
dados = regex.search('A Turma01 de Programação é muito fera')
print(dados)
# o circunflexo '^' no início do colchete '[]' é a negação da classe
regex = re.compile(r'ABC[^4-9]')
dados = regex.search('A Turma ABC103 de Programação é muito fera')
print(dados)

dados = regex.search('A Turma ABC400 de Programação é muito fera')
print(dados)
# a interrogação '?' significa ' o que precede esse caractere pode ou não aparecer'
regex = re.compile(r'ab?c')
dados = regex.search('abc')
print(dados)

dados = regex.search('ac')
print(dados)

dados = regex.search('c')
print(dados)

regex = re.compile(r'.?c')
dados = regex.search('c')
print(dados)

m = re.search(r'\w+@\w+', ' bla yzx abc@icen.ufpa.br las')
print(m)

m = re.search(r'\w+@\w+\.\w+(\.\w+)?', ' bla yzx abc@icen.ufpa.br las')
print(m)
