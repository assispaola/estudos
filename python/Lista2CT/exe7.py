valor = input("Digite um número de 0 a 99:")
num = int(valor)

# // é para divisão inteira (sem resto)
dezena = num//10
unidade = num%10

print(f"Dezena:{dezena}")
print(f"Unidade:{unidade}")