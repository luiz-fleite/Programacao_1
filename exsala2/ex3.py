s = input()
d = {}

for x in s:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(max(d, key=d.get), max(d.values()))
