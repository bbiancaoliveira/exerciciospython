print('-'*50)
print('              CÁLCULO DO SALÁRIO:')
print('-'*50)

listaContador = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while(1):
    venda = float(input("Digite o valor total de vendas [-1 para sair]: "))
    if venda == -1:
        break
    salario = 200
    porcentagem = 0.09
    valorBruto = (salario + (venda * porcentagem))
    #valorBruto = int('%.0f' % (salario + (venda * porcentagem)))
    print('Valor total do salário: R$', valorBruto)
    print('-' * 50)

    if (valorBruto >= 200 and valorBruto <= 299):
        listaContador[0] += 1

    if (valorBruto >= 300 and valorBruto <= 399):
        listaContador[1] += 1

    if (valorBruto >= 400 and valorBruto <= 499):
        listaContador[2] += 1

    if (valorBruto >= 500 and valorBruto <= 599):
        listaContador[3] += 1

    if (valorBruto >= 600 and valorBruto <= 699):
        listaContador[4] += 1

    if (valorBruto >= 700 and valorBruto <= 799):
        listaContador[5] += 1

    if (valorBruto >= 800 and valorBruto <= 899):
        listaContador[6] += 1

    if (valorBruto >= 900 and valorBruto <= 999):
        listaContador[7] += 1

    if (valorBruto >= 1000):
        listaContador[8] += 1

print('-'*50)
print('RELATÓRIO FINAL')
print('-'*50)

print('Qnt. vendedor por intervalo: $200 - $299: ', listaContador[0])
print('Qnt. vendedor por intervalo: $300 - $399: ', listaContador[1])
print('Qnt. vendedor por intervalo: $400 - $499: ', listaContador[2])
print('Qnt. vendedor por intervalo: $500 - $599: ', listaContador[3])
print('Qnt. vendedor por intervalo: $600 - $699: ', listaContador[4])
print('Qnt. vendedor por intervalo: $700 - $799: ', listaContador[5])
print('Qnt. vendedor por intervalo: $800 - $899: ', listaContador[6])
print('Qnt. vendedor por intervalo: $900 - $999: ', listaContador[7])
print('Qnt. vendedor por intervalo: $1000 - mais:', listaContador[8])

