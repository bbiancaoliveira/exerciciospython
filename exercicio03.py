print('-' * 55)
print('CÁLCULO DO PESO')
print('-' * 55)

sexo = int(input('Digite seu sexo: (1) Para Mulher  |  (2) Para Homem: '))

if sexo == 1:
    altura = float(input('Digite sua altura: '))
    pesomulher = (62.1 * altura) - 44.7
    print('Seu peso ideal é {:.1f} quilos'.format(pesomulher))
elif sexo == 2:
    altura = float(input('Digite sua altura: '))
    pesohomem =(72.7 * altura) - 58
    print('Seu peso ideal é {:.1f} quilos'.format(pesohomem))


