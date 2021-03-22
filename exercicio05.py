print('CÁLCULO DA MÉDIA')
print('-' * 30)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print('Voce foi Aprovado')
elif media < 7:
    print('Voce foi Reprovado')
elif media >= 10:
    print('Voce foi Aprovado com Distinçao')