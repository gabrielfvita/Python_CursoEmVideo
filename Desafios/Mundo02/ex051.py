termo = int(input('Digite o valor do 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
   
for c in range(1, 11):
    print(f'a{c} = {termo}')
    termo += razao