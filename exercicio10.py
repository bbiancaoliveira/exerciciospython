print('-'*50)
print('CALCULO DE PRESTAÇOES')
print('-'*50)
contador = 0
valorTotal = 0

def valorPagamento(valorPrestacao,diasAtraso):
    if diasAtraso == 0:
        valorPago = valorPrestacao
    if diasAtraso != 0:
        valorPago = (valorPrestacao + (valorPrestacao * 0.03) + ((valorPrestacao * 0.001) * diasAtraso))
    return valorPago

while (1):

    valorPrestacao = float(input('Insira o valor da prestaçao [0 para parar]: R$ '))

    if valorPrestacao == 0:
        break
    else:
        diasAtraso = float(input('Dias de atraso: '))
        print('Total a pagar: R$ {:.2f}'.format(valorPagamento(valorPrestacao, diasAtraso)))
        contador += 1
        valorTotal += valorPagamento(valorPrestacao, diasAtraso)
        print('-'*50)

print('-' * 50)
print('- RELATÓRIO DAS PRESTAÇOES:')
print('Quantidade de prestaçoes: ', contador)
print('Valor total pago: R$ {:.2f}'.format(valorTotal))


