frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
letraA = frase.count('A')
print('A letra "A" aparece {} vezes na frase.'.format(letraA))
print('A primeira letra "A" apareceu na posiçao {}'.format(frase.find('A')+1) )
print('A ultima letra "A" apareceu na posiçao {}'.format(frase.rfind('A')+1) )