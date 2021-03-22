print('AUMENTO DE SALÁRIO')
print('-' * 30)

salario = float(input('Digite seu salário: '))

if salario <= 280:
    salarioatual = salario + (salario * 20 / 100)
    porcent = '20%'
    reajuste = (salario/100) * 20

elif salario > 280 and salario <= 700:
    salarioatual = salario + (salario * 15 / 100)
    porcent = '15%'
    reajuste = (salario / 100) * 15

elif salario > 700 and salario <= 1500:
    salarioatual = salario + (salario * 10 / 100)
    porcent = '10%'
    reajuste = (salario / 100) * 10

else:
    salarioatual = salario + (salario * 5 / 100)
    porcent = '5%'
    reajuste = (salario / 100) * 5
print()
print('-' * 30)
print('DETALHAMENTO DO REAJUSTE')
print()
print('Salário anterior: R${:.2f}'.format(salario))
print('Porcentagem do reajuste:', porcent)
print('Valor do reajuste: R${:.2f}'.format(reajuste))
print('-' * 30)
print('Salário reajustado: R${:.2f}'.format(salarioatual))