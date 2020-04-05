valor = input("Valor à Vista: R$")
avista = float(valor)

valor = input("Valor Parcela 1: R$")
parcela = float(valor)


desconto = avista - parcela
percentual = (avista - parcela) / 100


print(f"Pagando à vista seu DESCONTO é de:{percentual} %")
print(f"Pagando à vista seu DESCONTO é de R$:{desconto}")
