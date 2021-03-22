print('-'*50)
print('ENTRADA DE VALORES')
print('-'*50)

numero = contador = soma = media = maior = menor = 0
lista = []
lista7 = 0

while (1):
    numero = float(input('Digite um valor [ou -1 para sair]: '))
    if numero == -1:
        break
    else:
        lista.append(numero)

    soma += numero
    contador += 1

    if numero < 7:
        lista7 += 1

media = soma / contador

acumuloMediaMaior = 0
for mediamaior in lista:
    if (mediamaior > media):
        acumuloMediaMaior += 1

print('-' * 50)
print('Quantidade de valores inseridos: {}'.format(contador))
print('-'*50)
print('Valores inseridos na ordem: ', lista)
print('-'*50)
print('Valores na ordem inversa:')

for elementolista in reversed(lista):
    print(elementolista)

print('-'*50)
print('Soma dos valores inseridos: {}'.format(soma))
print('-'*50)
print('Média dos valores inseridos: {:.2f}'.format(media))
print('-'*50)
print('Quantidade de valores acima da média: ', acumuloMediaMaior)
print('-'*50)
print('Quantidade de valores abaixo de 7:', (lista7))
print('-'*50)
print(' - FIM DO PROGRAMA')
