megabyte = float(input("Insira o valor do tamanho do arquivo em megabyte (MB): "))
mbps = float(input("Insira o valor da velocidade de internet em megabit por segundo (Mbps): "))

seg = megabyte * 8 / mbps
min = seg / 60

print("Tempo estimado de download em minutos: ", min)
