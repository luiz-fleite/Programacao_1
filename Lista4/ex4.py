
eq = {"ar-condicionado": 1600,
      "computador": 350,
      "chuveiro": 5000,
      "ferro": 1000,
      "lâmpada": 32,
      "lavadora-roupas": 600,
      "refrigerador": 350,
      "tv": 200}

b = {"verde": 0.5,
     "amarela": 0.53,
     "vermelha": 0.56}

# recebendo a bandeira dando a lista de opções
print("Bandeiras:\n", b.keys())
bandeira = input("Insira a bandeira: ")

# recebendo icms
icms = float(input("Insira o valor do icms em decimal: "))

# recebendo os equipamentos dando a lista de opções e salvando o kwh (energia utilizada)
n = int(input("Insira o número de equipamentos: "))
print("Equipamentos:\n", eq.keys())
kwh = []
for i in range(n):
    entrada_eq_t = input(f"Insira o equipamento {i + 1} e o tempo de uso médio diário em horas separado por espaço: ")
    equipamento, t = entrada_eq_t.split()[0], float(entrada_eq_t.split()[1])
    if equipamento in eq:
        kwh.append(eq[equipamento] * t / 1000)

# fazendo o calculo do total gasto e printando
print(f"Conta final: {(sum(kwh) * b[bandeira]) * (icms + 1):.2f}R$")
