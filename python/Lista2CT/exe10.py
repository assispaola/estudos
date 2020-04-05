valor = input("Distância Percorrida (metros):")
corrida = float(valor)

valor = input("Tempo (segundos):")
tempo = float(valor)

delta_s = corrida - 0
delta_t = tempo - 0
vm = delta_s/delta_t

# CONVERSÃO m/s para km/h > MULTIPLICA POR 3,6
# CONVERSÃO km/h para m/s > DIVIDE POR 3,6
km = vm * 3.6

print(f"VELOCIDADE MÉDIA EM m/s:{vm}")
print(f"VELOCIDADE MÉDIA EM Km/h:{km}")