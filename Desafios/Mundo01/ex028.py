from random import randint
numero = randint(0,5)

chute = int(input('Tente acertar o número entre 0 e 5:'))
if chute == numero:
    print('Você acertou, parabens!')
else:
    print('Você errou, tente novamente...')
print('O número era: {}'.format(numero))