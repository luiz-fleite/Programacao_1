import pandas as pd
import string

tabela = pd.read_excel("debate_band.xlsx", usecols='F')

# retirando toda a pontuação do DataFrame
pontuacao = string.punctuation
for p in pontuacao:
    tabela["Texto"] = tabela["Texto"].str.replace(p, '', regex=True)

# transformando todas as palavras para lower case e criando as listas
tabela["Texto"] = tabela["Texto"].str.lower().str.split(' ')

# criando listas pra receber as palavras e suas frequências
palavras = []
freqs = []
for linha in range(len(tabela["Texto"])):  # perpassando todas as linhas
    for p in tabela["Texto"].get(linha):  # perpassando todas as palavras da linha
        if p not in palavras:  # salvando uma palavra nova
            palavras.append(p)
            freqs.append(1)  # contando ela
        else:
            freqs[palavras.index(p)] += 1  # contando repetição de palavras

tabela2 = pd.DataFrame(list(zip(palavras, freqs)), columns=['Palavras', 'Frequência']).sort_values(['Frequência'], ascending=False)  # formando novo DataFrame

tabela2.to_excel("freq_palavras.xlsx", index=False)
