crg = {'wanderley Andrade': 5.4, 'Joelma': 9.8, 'Dona Onete': 8.5}
print(type(crg))
print(crg)
print(crg['Joelma'])

crg['Joelma'] = 4.6
crg['Dona Onete'] = 5.8
print(crg)

for x in crg:
    print(x)

for x in crg.values():
    print(x)

print("wanderley Andrade" in crg)
print('noe' in crg)

d = {'a':0, 'b':1, 'c':2}
t = d.items()

print(t)

print(list(crg.items()))
print(list(crg.keys()))
print(list(crg.values()))

print(crg.get("Joelma"))
print(crg.get("José"))

for nome, numero in crg.items():
    print(nome, numero, sep=' ')
