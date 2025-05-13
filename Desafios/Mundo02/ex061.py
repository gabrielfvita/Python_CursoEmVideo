termo = int(input('Digite o valor do 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
while c <= 10:
    print(f'a{c} = {termo}')
    termo += razao
    c += 1