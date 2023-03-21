print("Égua" in "Égua acho que vai chover")

a = "Égua acho que vai chover"
print(a.find("acho"))
print(a.find("max"))

notas = "34; 13; 97"
print(notas.split(";"))
print(a.split())
print(a.replace("vai chover", "vou tomar açaí"))
print(a)

a = "Égua acho que vai chover"
print(list(a))

b = list(a)
c = "".join(b)
print(c)