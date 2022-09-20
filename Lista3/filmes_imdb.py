import imdb
import csv

ia = imdb.IMDb()

#name = "Pulp Fiction"
#search = ia.search_movie(name)
#print(search)
codes = [20880628, 10872600, 3501632, 9419884, 7131622]
colunas = ['codes', 'title', 'year', 'genres', 'kind']
linhas = []

for i in range(5):
    linha = []
    series = ia.get_movie(codes[i])
    linha.append(codes[i])
    for j in range(1, 5):
        linha.append(series.data[colunas[j]])
    linhas.append(linha)

with open('filmes.csv', 'w', newline="") as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(colunas)
    write.writerows(linhas)
