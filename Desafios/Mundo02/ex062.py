termo = int(input('Digite o valor do 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
resposta = 1
c = 1
while c <= 10:
    print(f'a{c} = {termo}')
    termo += razao
    c += 1
while resposta != 0:
    resposta = int(input('Deseja ver mais quantos termos? '))
    for cont in range(c,c+resposta):
        print(f'a{cont} = {termo}')
        termo += razao
        c += 1
print('PA Finalizada!')