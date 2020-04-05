# Fórmula Área: A = pi * r²
# Fórmula Perímetro: 2pi * r

pi = 3.141592

valor = input("Digite o valor do Raio:")
r = float(valor)

areaperimetro = pi*r**2
perimetro = 2*pi*r

print(f"Área:{areaperimetro}")
print(f"Perimetro:{perimetro}")