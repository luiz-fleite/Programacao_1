t1 = 20,
print(type(t1))

t2 = 40,
t3 = t1 + t2, 3, 4, 6
print(t3)

nova_tupla = tuple('teste')
nova_tupla1 = 'teste',
print(nova_tupla)
print(nova_tupla1)

a = (5, 'outubro', 9.5, 1)
a = list(a)
print(a)

nome_produto = 'carne'
preco = 22.9
qtd_comprada = 1.1
carne = (nome_produto, preco, qtd_comprada)
print(carne)

compras_efetuadas = [
  ('arroz', 3.49, 3),
  ('feijão', 2.99, 2),
  ('tomate', 1.99, 0.8)
]

for nome_produto, preco, qtd_comprada in  compras_efetuadas:
  print(f'Nome: {nome_produto}\tPreço: {preco}\tQtd comprada: {qtd_comprada}')