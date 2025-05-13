from random import randint
numero = randint(0,10)
contador = 1
chute = int(input('Tente acertar o número entre 0 e 10: '))
while chute != numero:
    chute = int(input('Não foi dessa vez... digite outro numero: '))
    contador += 1
print(f'Parabéns! Você acertou com {contador} tentativa(s). \nO número era: {numero}!')