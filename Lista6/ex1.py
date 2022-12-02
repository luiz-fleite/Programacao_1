import re

telefones_coletados = re.findall(r"\(?\d{2,3}[ )\-\n]? ?\d{5}[ \-\n]?\d{4}",
                               "(091)91234 5678 91 91234 5678 91-91234-5678 (91) 91234-5678 91 98039 4004")
print(telefones_coletados)

numeros_limpos = [re.sub(r"^\D?0|\D", "", x) for x in telefones_coletados]
print(numeros_limpos)

telefones_formatados = [f"({num[0:2]}) {num[2:7]} {num[7:]}" for num in numeros_limpos]
print(telefones_formatados)
