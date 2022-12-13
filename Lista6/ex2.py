import pandas as pd

# recebendo o arquivo
df = pd.read_excel("github-ranking.xlsx")

# salvando apenas as linhas com "Python" na coluna "language" em outro df para trabalhar com ele
df_python = df.loc[df["language"] == "Python"]

# criando o csv apenas com python
df_python.to_csv("only_python.csv", index=False)

# criando o ranking de python por stars no csv
df_python.sort_values(by="stars", ascending=False, inplace=False).head(50).to_csv("py_stars_ranking.csv")
#.reset_index() poderia ser usado

# criando o ranking de python por forks no csv
df_python.sort_values(by="forks", ascending=False, inplace=False).head(50).to_csv("py_forks_ranking.csv")
