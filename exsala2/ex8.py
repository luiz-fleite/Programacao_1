
mat = []
for i in range(3):
    l = []
    for j in range(4):
        l.append(i * j)
    mat.append(l)

print(mat)

mat = [[i * j for j in range(4)] for i in range(3)]
print(mat)
