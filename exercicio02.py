print('-' * 50)
print('CÁLCULO DA MÉDIA')
print('-' * 50)

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('-' * 50)
print('A média entre {:.1f} | {:.1f} | {:.1f} | {:.1f} é igual a {:.1f}'.format(nota1, nota2, nota3, nota4, media))
