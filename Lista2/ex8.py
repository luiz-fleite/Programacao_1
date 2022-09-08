data = str(input("Insira a data no formato dd/mm/aaaa: "))
dia, mes, ano = int(data[:2]), int(data[3:5]), int(data[6:])

mes30 = [4, 6, 11]

if (1 > mes > 12) or (1 > dia > 31) or (mes == 2 and dia > 29) or (dia > 30 and mes in mes30)\
        or (ano % 4 != 0 and mes == 2 and dia == 29):
    print("Data inválida.")
else:
    print("Data válida.")
