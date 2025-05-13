print('-------- Banco --------')

valor = int(input('Informe um valor para sacar: R$'))

notas50 = valor // 50
resto = valor % 50
notas20 = resto // 20
resto = resto % 20
notas10 = resto // 10
notas1 = resto % 10

if notas50 > 0:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 > 0:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 > 0:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 > 0:
    print(f'Total de {notas1} cédulas de R$1')
print('-----------------------')