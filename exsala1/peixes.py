import csv

colunas = ['peixes', 'peso', 'barraca', 'valor por quilo']
linhas = [['tambaqui', 3.2, '45', 20.4], 
         ['pirarucu', 4.5, '63', 30], 
         ['filhote', 10.5, '54', 21],
         ['surubim', 3.0, '12', 15], 
         ['pescada amarela', 9.2, '13', 12],
         ['acari', 3.4, '14', 9]]

with open('GFG.csv', 'w', newline='') as f:
  write = csv.writer(f)
  write.writerow(colunas)
  write.writerows(linhas)
