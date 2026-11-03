salario = float(input ('salario atual: R$'))
percentual = float(input('informe o digito para percentual: '))
percentual = percentual / 100

aumento = salario_atual * percentual

reajuste = 0.15
processamento = salario + (salario * reajuste)
print(f'salario final: R$',processamento)

