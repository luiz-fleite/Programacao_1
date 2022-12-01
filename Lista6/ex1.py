import re

numeros_coletados = re.findall(r"\(?\d{2,3}[ )\-\n]? ?\d{5}[ \-\n]?\d{4}",
                               "(091)91234 5678 91 91234 5678 91-91234-5678 (91) 91234-5678")
print(numeros_coletados)
