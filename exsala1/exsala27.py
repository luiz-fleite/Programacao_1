lista_de_listas = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
lista_final = [item for list in lista_de_listas for item in list]
print(lista_final)
