import pandas as pd
nomes = ['Ana', 'Bruno', 'Carla']
idades = [21, 20, 22]
dados = list(zip(nomes, idades))
print(dados)
df = pd.DataFrame(data = dados)
print(df)
print(df[0][0], df[0][1], df[0][2])

dados = {'Nome': ['Ana', 'Bruno', 'Carla'], 'idade': [21, 20, 22]}
print(dados)
df = pd.DataFrame(data = dados)
print(df)

nomes = ['Ana', 'Bruno', 'Carla']
idades = [21, 20, 22]
dados = list(zip(nomes, idades))
print(dados)
colunas = ['Nome', 'Idade']
linhas = ['A', 'B', 'C']
df = pd.DataFrame(data = dados, columns = colunas, index = linhas)
print(df)

print(df.index)
print(df.columns)

print(df.ndim)
print(df.shape)
print(df.size)
print(df.empty)

print(df['Nome']['A'], df['Nome']['B'], df['Nome']['C'])

print(df)
print(df.T)
print(df.at['C', 'Nome'])
print(df.at['C', 'Idade'])
# df.at acessa apenas rotulos, numeros dão ValueError

df['Sexo'] = 'F'
print(df)

df['Sexo'] = ['F', 'M', 'F']
print(df)

dados2 = [ {'Nome': 'Carla', 'Idade': 22, 'Sexo': 'F'}, {'Nome': 'Daniel', 'Idade': 18, 'Sexo': 'M'}]
# df2 = df.append(dados2, ignore_index = False)
df2 = df.append(dados2, ignore_index = True)
print(df2)

df.loc['B'] = ['Bento', 22, 'M']
df.loc['C'] = ['Carla', 22, 'F']
df.loc['D'] = ['Daniela', 18, 'F']
print(df)

df2.iloc[1] = ['Bruno', 19, 'M']
df2.iloc[3] = ['Daniel', 18, 'M']
print(df2)

df.at['C', 'Idade'] = 20
df.iat[0, 1] = 17
print(df)

# drop remove valores
# inplace = False faz com que o df não seja modificado, apenas retorne um df naquela linha com a modificação
# caso contrario, ele é modficado
df.drop(index = ['A', 'D'], columns = ['Sexo'], inplace = True)
print(df)

df2['Idade'] += 1
print(df2)

resultado = list(df2['Idade'] >= 18)
print(resultado)

resultado = list(df2['Sexo'] == 'F')
print(resultado)

df2.sort_values(by = 'Idade', ascending = False, inplace = True)
print(df2)

df2.to_csv('dados.csv')

df3 = pd.read_csv('dados.csv', index_col = 0, header = 0)
print(df3)