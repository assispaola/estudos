rm = int(inout("RM: "))

acumulador = 0

resto = rm % 10 #resto da divisão
acumulador = acumulador + resto
rm = rm // 10 #quociente inteiro da divisão

resto = rm % 10
acumulador = acumulador + resto
rm = rm // 10

resto = rm % 10
acumulador = acumulador + resto
rm = rm // 10

print("Resultado: ", acumulador)