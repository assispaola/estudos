valor = input("Sálario ANTES do Aumento: R$")
salarioantes = float(valor)

valor = input("Sálario APÓS do Aumento: R$")
salariodepois = float(valor)

percentual_aumento = (salariodepois - salarioantes) / 100


print(f"Seu percentual de aumento foi de:{percentual_aumento} %")
