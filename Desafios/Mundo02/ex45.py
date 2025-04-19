from random import randint
from random import choice

escolha_usuario = int(input(' 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n Informe o número da sua escolha: '))

opcoes = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = choice(opcoes)
print(escolha_computador)

if escolha_usuario == 1 and escolha_computador == 'Pedra':
    resultado = 'O jogo empatou!'
elif escolha_usuario == 1 and escolha_computador == 'Papel':
    resultado = 'Você perdeu!'
elif escolha_usuario == 1 and escolha_computador == 'Tesoura':
    resultado = 'Você ganhou!'
elif escolha_usuario == 2 and escolha_computador == 'Pedra':
    resultado = 'Você ganhou!'
elif escolha_usuario == 2 and escolha_computador == 'Papel':
    resultado = 'O jogo empatou!'
elif escolha_usuario == 2 and escolha_computador == 'Tesoura':
    resultado = 'Você perdeu!'
elif escolha_usuario == 3 and escolha_computador == 'Pedra':
    resultado = 'Você perdeu!'
elif escolha_usuario == 3 and escolha_computador == 'Papel':
    resultado = 'Você ganhou!'
elif escolha_usuario == 3 and escolha_computador == 'Tesoura':
    resultado = 'O jogo empatou!'
else:
    resultado = 'Você digitou uma opção inválida! Não foi possível prosseguir...'

if escolha_usuario == 1:
    escolha_usuario = 'Pedra'
elif escolha_usuario == 2:
    escolha_usuario = 'Papel'
elif escolha_usuario == 3:
    escolha_usuario = 'Tesoura'
else:
    escolha_usuario = 'Opção inválida'

print('------ Jokenpô ------')
print(f'Você: {escolha_usuario}')
print(f'Computador: {escolha_computador}')
print(f'RESULTADO: {resultado}')