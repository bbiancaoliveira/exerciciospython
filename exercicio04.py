print('-' * 40)
print('CÁLCULO DO SALÁRIO')
print('-' * 40)
valorhora = float(input('Quanto voce ganha por hora? '))
horastrab = float(input('Quantas horas voce trabalhou? '))

salarioB = valorhora * horastrab

ir = (11/100.0 * salarioB)
inss = (8/100.0 * salarioB)
sindicato = (5/100.0 * salarioB)

totaldesc = ir + inss + sindicato
salarioL = salarioB - totaldesc

print('-' * 40)
print('Salário bruto R$ %.2f' % (salarioB))
print('-' * 40)
print('Valor dos impostos:')
print('IR 11%: R${:.2f}'.format(ir))
print('INSS 8%: R${:.2f}'.format(inss))
print('Sindicato 5%: R${:.2f}'.format(sindicato))
print('-' * 40)
print('Salário líquido R$ %.2f' % (salarioL))
print('-' * 40)

