valor = input("Valor do Produto: R$")
preco = float(valor)

valor = input("Porcentagem Desconto: %")
desconto = float(valor)

# calculo percentual de desconto valor * desconto/100:
percentual = preco * desconto/100

novopreco = preco - percentual
aumento = preco + percentual

print(f"VALOR DO DESCONTO É R$: {percentual}")
print(f"PREÇO TOTAL COM DESCONTO É R$: {novopreco}")
print(f"PREÇO COM AUMENTO É R$: {aumento}")
